import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from PySide6.QtGui import QColor
from mainwindow import Ui_MainWindow
import re
import time
import threading
import ast
#Geräte importieren
from sg390serial import Sg390 as Sgclass
from ke2010gpib import Ke2010 as Vmclass
from pulseblaster_esrpro import PulseBlasterEsrpro as Pbclass
#from virtual_vm import Vmvirtual as Vmclass

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
        self.ui.toggle_recording_pushbutton.clicked.connect(self.toggle_recording_clicked)
        self.ui.tag_event_pushbutton.clicked.connect(self.tag_event)
        #Externer PulseBlaster Signalgenerator
        self.ui.external_pulse_radiobutton.toggled.connect(self.toggle_external_pulse)
        self.ui.external_start_pushbutton.clicked.connect(self.external_start_clicked)
        self.ui.external_stop_pushbutton.clicked.connect(self.external_stop_clicked)

        #Flags setzen und Timer für Aktualisierung implementieren
        self.flag_display_voltage = False
        self.flag_recording = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.voltage_display)
        self.timer.timeout.connect(self.record)
        self.tick_length = 200
        self.timer.start(self.tick_length)
        self.timestamp = time.time()

        #Recording functionality init
        self.rfile = None

        #Vorfüllen der Verbindungen aus connectioncache Datei
        prev_conn_cache = open("connectioncache","r+")
        prev_conn = ast.literal_eval(prev_conn_cache.read())
        if prev_conn["sg"]!="":
            self.ui.target_ip_line.setText(prev_conn["sg"])
        if prev_conn["ro"]!="":
            self.ui.readout_connect_line.setText(prev_conn["ro"])
            
        
    #Signalgenerator verbinden
    def connect_microwave_clicked(self):
        #Inhalt aus Lineedit nehmen
        target_ip = self.ui.target_ip_line.text()
        try:
            self.sg = Sgclass(target_ip)
            sg_id = self.sg.check_connection()
            #Bei Erfolg durchgeben
            self.info_message("Connected to "+sg_id+" at "+target_ip)
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
            self.warning_message("Could not connect to this adress")
        
    
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
                        self.warning_message("Stepsize must be smaller than Sample width") 
                else:
                    self.warning_message("Upper Bound must be higher than lower Bound")                 
            else:
                self.warning_message("Invalid Frequency Format: Enter Frequency as Integer or Float")
        else:
            self.warning_message("Units must be specified")

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
                try:
                    self.sg.set_amplitude(target_ampl,ampl_unit)
                    self.sg.set_frequency(target_freq,freq_unit)
                except:
                    self.error_message("Could not apply these Settings to Device")
            else:
                self.warning_message("Invalid Settings Format: Enter as Integer or Float")
        else:
            self.warning_message("Units must be specified")

    def dump_signal_settings_clicked(self):
        try:
            sg_id = self.sg.check_connection()
        except:
            self.error_message("Did not receive Response from Device, try reconnecting")
            return
        sg_freq = self.sg.get_frequency()
        sg_ampl = self.sg.get_amplitude()
        sg_modul = self.sg.get_modulation_status()
        self.info_message("Device Id: "+sg_id)
        self.info_message("Frequency: "+sg_freq+"Hz")
        self.info_message("Amplitude: "+sg_ampl+"dBm")
        self.info_message("Modulation: "+str(sg_modul))

    def pulse_toggle_clicked(self):
        pfunc = self.ui.pulse_function_combobox.currentText()
        pper = self.ui.pulse_period_line.text()
        pwid = self.ui.pulse_width_line.text()
        punit = self.ui.pulse_timeunits_combobox.currentText()
        #Input filtern
        sample_re = "(^[0-9]+$)|(^[0-9]*\.[0-9]+$)"
        if re.search(sample_re,pper) and re.search(sample_re,pwid):
            try:
                self.sg.set_pulse_period(pper,punit)
                self.sg.set_pulse_width(pwid,punit)
                self.sg.switch_pulsed_status()
            except:
                self.error_message("Could not apply these Settings to Device")
        else:
            self.warning_message("Invalid period settings format")

    def dump_pulse_info_clicked(self):
        pper = self.sg.get_pulse_period("us")
        pwid = self.sg.get_pulse_width("us")
        self.ui.output_textedit.append("Pulse Period: " +pper+" us")
        self.ui.output_textedit.append("Pulse Width: " +pwid+" us")

    def dump_err_clicked(self):
        sg_id = self.sg.check_connection()
        while True:
            errcode = self.sg.get_last_error()
            self.ui.output_textedit.append(sg_id+" Error: " +str(errcode))
            if errcode == False:
                break

    def readout_connect_clicked(self):
        target = self.ui.readout_connect_line.text()
        try:
            self.vm = Vmclass(target)
            vm_id = self.vm.check_connection()
            #Bei Erfolg durchgeben
            self.info_message("Connected to "+vm_id+" at "+target)
            #Anfangen den aktuellen Wert des Multimeters anzuzeigen
            self.flag_display_voltage = True
        except:
            self.error_message("Could not connect to this Adress")
        
    
    def voltage_display(self):
        if self.flag_display_voltage==True:
            new_voltage = self.vm.read_voltage()
            #Stepdauer in ms
            dur = self.tick_length
            self.ui.readout_plot.push_new_value(new_voltage,dur)
            #Messen der Plotdauer
            #newtime = time.time()
            #self.timestamp = newtime - self.timestamp
            #print(self.timestamp)

    def toggle_recording_clicked(self):
        if self.flag_recording == False:
            target = self.ui.record_target_line.text()
            if re.search("\.csv",target) != None:
                self.rfile = open(target,"a")
                self.flag_recording = True
            elif target == "":
                self.rfile = open("recording_"+str(time.time())+".csv","a")
                self.flag_recording = True
            self.record("start")
            self.info_message("Started Recording")
        elif self.flag_recording == True:
            self.record("stop")
            self.flag_recording = False
            self.rfile.close()
            self.info_message("Stopped Recording")

    #Writes line to opened .csv including value, unit and a string flag for marking events
    def record(self,tag = "0"):
        if self.flag_recording == True:
            try:
                self.rfile.write( str(self.vm.read_voltage()) + "," + str(self.vm.read_unit()) + "," + str(time.time()) + "," + tag + "\n")
            except:
                self.ui.output_textedit.append("Could not write to file")

    def tag_event(self):
        try:
            self.record(str(self.ui.tag_text_line.text()))
            self.info_message("Event tagged as " + str(self.ui.tag_text_line.text()))
        except:
            self.error_message("Could not tag event")

    def toggle_external_pulse(self):
        state = self.ui.external_pulse_radiobutton.isChecked()
        if state == True:
            self.pb = Pbclass()
            self.pb.check_connection()
        elif state == False:
            self.pb.disconnect()

    def external_start_clicked(self):
        if self.pb.is_running() == True:
            self.warning_message("PulseBlaster already running, try stopping it before running new Program")
        elif self.pb.is_running() == False:
            self.pb.program()
            self.pb.start()
            self.info_message("PulseBlaster executing program")
            
    def external_stop_clicked(self):
        if self.pb.is_running() == True:
            self.pb.stop()
            self.info_message("PulseBlaster stopped")
        elif self.pb.is_running() == False:
            self.warning_message("PulseBlaster already stopped")
            
        
    

    def info_message(self,message):
        self.ui.output_textedit.setTextColor(QColor(0,255,255))      
        self.ui.output_textedit.append(message)
    def warning_message(self,message):
        self.ui.output_textedit.setTextColor(QColor(255,255,0))      
        self.ui.output_textedit.append(message)
    def error_message(self,message):
        self.ui.output_textedit.setTextColor(QColor(255,0,0))      
        self.ui.output_textedit.append(message)    

#App Loop
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
