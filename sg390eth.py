import vxi11

#Erzeugt einen Signalgenerator als Klasse aus IP im string Format
class Sg390(vxi11.Instrument):
    supported_frequnits=["Hz","kHz","MHz","GHz"]
    supported_amplunits=["dBm","rms","Vpp"]
    supported_timeunits=["ns","us","ms","s"]
    supported_pulse_functions=["square","prbs"]
    #Funktionsdictionary
    func_dict = {"square":"3","prbs":"4"}
    def __init__(self,target_ip):
        super().__init__(target_ip)

    def check_connection(self):
        return self.ask("*IDN?")

    def set_amplitude(self,value,unit):
        self.write("AMPR"+" "+str(value)+" "+unit)

    def set_frequency(self,value,unit):
        self.write("FREQ"+" "+str(value)+" "+unit)
        
    def get_amplitude(self, unit = "dBm"):
        ampl = self.ask("AMPR?" + " " + unit)
        return ampl
        
    def get_frequency(self, unit = "Hz"):
        freq = self.ask("FREQ?" + " " + unit)
        return freq

    def switch_pulsed_status(self):
        is_modulated = self.ask("MODL?")
        try:
            if is_modulated == "0":
                self.write("MODL 1")
                self.write("TYPE 4")
            if is_modulated == "1":
                mod_type = self.ask("TYPE?")
                if mod_type == "4":
                    self.write("MODL 0")
                else:
                    self.write("TYPE 4")
        except:
            print("Error in determining or applying modulation")

    def get_modulation_status(self):
        is_modulated = self.ask("MODL?")
        if is_modulated == "1":
            mod_type = self.ask("TYPE?")
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
            self.write("PFNC"+" "+self.func_dict[func])
        else:
            raise Exception("Unsupported pulse function")

    def get_pulse_function(self):
        pfunc = self.ask("PFNC?")
        #dictionary implementieren
        return pfunc

    def set_pulse_period(self,value,unit):
        self.write("PPER"+" "+str(value)+" "+unit)

    def get_pulse_period(self,unit="s"):
        pper = self.ask("PPER?"+" "+unit)
        return pper

    def set_pulse_width(self,value,unit):
        self.write("PWID"+" "+str(value)+" "+unit)

    def get_pulse_width(self,unit="s"):
        pwid = self.ask("PWID?"+" "+unit)
        return pwid

    def get_last_error(self):
        errcode = self.ask("LERR?")
        if errcode == "0":
            errcode = False
        return errcode
        

#from sg390 import Sg390 as sgclass
#sg = sgclass("169.254.184.198")
