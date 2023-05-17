import pyvisa
import re

#Class Implementing Communication with a SG394 signal generator over a VISA Interface
class Sg390(pyvisa.resources.SerialInstrument):
    #Lists passed to communicate compatible units
    supported_frequnits=["Hz","kHz","MHz","GHz"]
    supported_amplunits=["dBm","rms","Vpp"]
    supported_timeunits=["ns","us","ms","s"]
    supported_pulse_functions=["square","prbs"]
    #Dictionary to translate pulse functions into their associated integer code in the instrument
    func_dict = {"square":"3","prbs":"4"}

    def __init__(self,target_port):
        #Initialize pyvisa
        rm = pyvisa.ResourceManager()
        self.device = rm.open_resource(target_port)
        self.device.baud_rate=115200
        
    def check_connection(self):
        tmp = self.device.query("*IDN?")
        #Strip linebreaks
        tmp = re.sub("\n","",tmp)
        return tmp

    def set_amplitude(self,value,unit):
        self.device.write("AMPR"+" "+str(value)+" "+unit)

    def set_frequency(self,value,unit):
        self.device.write("FREQ"+" "+str(value)+" "+unit)
        
    def get_amplitude(self, unit = "dBm"):
        ampl = self.device.query("AMPR?" + " " + unit)
        return ampl
        
    def get_frequency(self, unit = "Hz"):
        freq = self.device.query("FREQ?" + " " + unit)
        return freq

    def switch_pulsed_status(self):
        is_modulated = self.device.query("MODL?")
        try:
            if is_modulated == "0":
                self.device.write("MODL 1")
                self.device.write("TYPE 4")
            if is_modulated == "1":
                mod_type = self.device.query("TYPE?")
                if mod_type == "4":
                    self.device.write("MODL 0")
                else:
                    self.device.write("TYPE 4")
        except:
            print("Error in determining or applying modulation")

    def get_modulation_status(self):
        is_modulated = self.device.query("MODL?")
        if is_modulated == "1":
            mod_type = self.device.query("TYPE?")
            if mod_type == "0":
                return (True,"AM")
            if mod_type == "1":
                return (True,"FM")
            if mod_type == "2":
                return (True,"PhM")
            if mod_type == "3":
                return (True,"Sweep")
            if mod_type == "4":
                return (True,"Pulsed")
        else:
            return (False,None)
            

    def set_pulse_function(self,func):
        is_modulated = self.get_modulation_status()
        if is_modulated != (True,"Pulsed"):
            raise Exception("Trying to set Pulse Function on unpulsed Signal")
        if func in self.supported_pulse_functions:
            self.device.write("PFNC"+" "+self.func_dict[func])
        else:
            raise Exception("Unsupported pulse function")

    def get_pulse_function(self):
        pfunc = self.device.query("PFNC?")
        #dictionary implementieren
        return pfunc

    def set_pulse_period(self,value,unit):
        self.device.write("PPER"+" "+str(value)+" "+unit)

    def get_pulse_period(self,unit="s"):
        pper = self.device.query("PPER?"+" "+unit)
        return pper

    def set_pulse_width(self,value,unit):
        self.device.write("PWID"+" "+str(value)+" "+unit)

    def get_pulse_width(self,unit="s"):
        pwid = self.device.query("PWID?"+" "+unit)
        return pwid

    def get_last_error(self):
        errcode = self.device.query("LERR?")
        if errcode == "0\r\n":
            errcode = False
        return errcode