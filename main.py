import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from mainwindow import Ui_MainWindow
import re
import time
import threading
#Geräte importieren
from sg390serial import Sg390 as Sgclass
from ke2010gpib import Ke2010 as Vmclass

class MainWindow(QMainWindow):
    def __init__(self):
        #Initialisierung der grafischen Oberfläche
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Signal Handling
        self.ui.try_ip_pushbutton.clicked.connect(self.connect_microwave_clicked)
        self.ui.sample_frequency_pushbutton.clicked.connect(self.sample_frequency_clicked)
        self.ui.signal_setting_pushbutton.clicked.connect(self.signal_settings_clicked)
        self.ui.dump_signal_setting_pushbutton.clicked.connect(self.dump_signal_settings_clicked)
        self.ui.pulse_toggle_pushbutton.clicked.connect(self.pulse_toggle_clicked)
        self.ui.dump_pulse_info_pushbutton.clicked.connect(self.dump_pulse_info_clicked)
        self.ui.dump_err_pushbutton.clicked.connect(self.dump_err_clicked)
        self.ui.readout_connect_pushbutton.clicked.connect(self.readout_connect_clicked)

        #Flags setzen und Timer für Aktualisierung implementieren
        self.flag_display_voltage = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.voltage_display)
        self.tick_length = 100
        self.timer.start(self.tick_length)
        self.timestamp = time.time()
        
    #Signalgenerator verbinden
    def connect_microwave_clicked(self):
        #Inhalt aus Lineedit nehmen
        target_ip = self.ui.target_ip_line.text()
        #Prüfen ob valide IP-Adresse eingegeben wurde
        #ip_re = "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
        #if re.search(ip_re,target_ip):
        try:
            self.sg = Sgclass(target_ip)
            sg_id = self.sg.check_connection()
            #Bei Erfolg durchgeben
            self.ui.output_textedit.appendPlainText("Connected to "+sg_id+" at "+target_ip)
            #Auswahlboxen füllen
            frequnits = self.sg.supported_frequnits
            amplunits = self.sg.supported_amplunits
            timeunits = self.sg.supported_timeunits
            pulsefuncs = self.sg.supported_pulse_functions
            self.ui.sample_units_combobox.addItems(frequnits)
            self.ui.frequency_units_combobox.addItems(frequnits)
            self.ui.amplitude_units_combobox.addItems(amplunits)
            self.ui.pulse_timeunits_combobox.addItems(timeunits)
            self.ui.pulse_function_combobox.addItems(pulsefuncs)
        except:
            self.ui.output_textedit.appendPlainText("Could not connect to this Adress")
        
    
    #Frequenzabtastung
    def sample_frequency_clicked(self):
        sample_from = self.ui.from_frequency_line.text()
        sample_to = self.ui.to_frequency_line.text()
        sample_step = self.ui.stepsize_frequency_line.text()
        sample_unit = self.ui.sample_units_combobox.currentText()
        #Frequenzen entweder als Integer oder punktseparierter Float
        sample_re = "(^[0-9]+$)|(^[0-9]*\.[0-9]+$)"
        #Input bereinigen und nach Bestehehn Sampling durchführen
        if sample_unit != "":
            if re.search(sample_re,sample_from) and re.search(sample_re,sample_to) and re.search(sample_re,sample_step):
                if float(sample_from) < float(sample_to):
                    if float(sample_step) < float(sample_to) - float(sample_from):
                        target_freqs = [float(sample_from) + x * float(sample_step) for x in range(int((float(sample_to)-float(sample_from))//float(sample_step)))]
                        j=0
                        for i in target_freqs:
                            #print("Sampled" + str(i) + sample_unit)
                            #time.sleep(0.01) #Delay zum Debuggen
                            self.sg.set_frequency(i,sample_unit)
                            #Progress-Bar Aktualisieren
                            j+=1
                            self.ui.sampler_progress.setValue(100*j/len(target_freqs))
                    else:
                        self.ui.output_textedit.appendPlainText("Stepsize must be smaller than Sample width") 
                else:
                    self.ui.output_textedit.appendPlainText("Upper Bound must be higher than lower Bound")                 
            else:
                self.ui.output_textedit.appendPlainText("Invalid Frequency Format: Enter Frequency as Integer or Float")
        else:
            self.ui.output_textedit.appendPlainText("Units must be specified")

    #Schnelleinstellungen

    def signal_settings_clicked(self):
        target_ampl = self.ui.signal_amplitude_line.text()
        target_freq = self.ui.signal_frequency_line.text()
        #Match float or int
        settings_re = "(^-?[0-9]+$)|(^-?[0-9]*\.[0-9]+$)"
        ampl_unit = self.ui.amplitude_units_combobox.currentText()
        freq_unit = self.ui.frequency_units_combobox.currentText()
        if ampl_unit != "" and freq_unit != "":
            if re.search(settings_re,target_ampl) and re.search(settings_re,target_freq):
                #Mit richtiger Funktion ersetzen
                self.sg.set_amplitude(target_ampl,ampl_unit)
                self.sg.set_frequency(target_freq,freq_unit)
            else:
                self.ui.output_textedit.appendPlainText("Invalid Settings Format: Enter as Integer or Floar")
        else:
            self.ui.output_textedit.appendPlainText("Units must be specified")

    def dump_signal_settings_clicked(self):
        try:
            sg_id = self.sg.check_connection()
        except:
            self.ui.output_textedit.appendPlainText("Did not receive Response from Device, try reconnecting")
            return
        sg_freq = self.sg.get_frequency()
        sg_ampl = self.sg.get_amplitude()
        sg_modul = self.sg.get_modulation_status()
        self.ui.output_textedit.appendPlainText("Device Id: "+sg_id)
        self.ui.output_textedit.appendPlainText("Frequency: "+sg_freq+"Hz")
        self.ui.output_textedit.appendPlainText("Amplitude: "+sg_ampl+"dBm")
        self.ui.output_textedit.appendPlainText("Modulation: "+str(sg_modul))

    def pulse_toggle_clicked(self):
        pfunc = self.ui.pulse_function_combobox.currentText()
        pper = self.ui.pulse_period_line.text()
        pwid = self.ui.pulse_width_line.text()
        punit = self.ui.pulse_timeunits_combobox.currentText()
        #Input filtern
        sample_re = "(^[0-9]+$)|(^[0-9]*\.[0-9]+$)"
        if re.search(sample_re,pper) and re.search(sample_re,pwid):
            self.sg.set_pulse_period(pper,punit)
            self.sg.set_pulse_width(pwid,punit)
            self.sg.switch_pulsed_status()
        else:
            self.ui.output_textedit.appendPlainText("Invalid period settings format")

    def dump_pulse_info_clicked(self):
        pper = self.sg.get_pulse_period("us")
        pwid = self.sg.get_pulse_width("us")
        self.ui.output_textedit.appendPlainText("Pulse Period: " +pper+" us")
        self.ui.output_textedit.appendPlainText("Pulse Width: " +pwid+" us")

    def dump_err_clicked(self):
        sg_id = self.sg.check_connection()
        while True:
            errcode = self.sg.get_last_error()
            self.ui.output_textedit.appendPlainText(sg_id+" Error: " +str(errcode))
            if errcode == False:
                break

    def readout_connect_clicked(self):
        target = self.ui.readout_connect_line.text()
        try:
            self.vm = Vmclass(target)
            vm_id = self.vm.check_connection()
            #Bei Erfolg durchgeben
            self.ui.output_textedit.appendPlainText("Connected to "+vm_id+" at "+target)
            #Anfangen den aktuellen Wert des Multimeters anzuzeigen
            self.flag_display_voltage = True
        except:
            self.ui.output_textedit.appendPlainText("Could not connect to this Adress")
        
    
    def voltage_display(self):
        if self.flag_display_voltage==True:
            new_voltage = self.vm.read_voltage()
            #Stepdauer in ms
            dur = self.tick_length
            self.ui.readout_plot.push_new_value(new_voltage,dur)
            #Messen der Plotdauer
            newtime = time.time()
            self.timestamp = newtime - self.timestamp
            print(self.timestamp)

#App Loop
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())