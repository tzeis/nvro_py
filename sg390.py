import vxi11

#Erzeugt einen Signalgenerator als Klasse aus IP im string Format
class Sg390(vxi11.Instrument):
    supported_frequnits=["Hz","kHz","MHz","GHz"]
    supported_amplunits=["dBm","Vrmf","Vpp"]
    def __init__(self,target_ip):
        super().__init__(target_ip)

    def set_amplitude(self,value,unit):
        self.write("AMPR"+" "+str(value)+" "+unit)

    def set_frequency(self,value,unit):
        self.write("FREQ"+" "+str(value)+" "+unit)
        
    def get_amplitude(self):
        self.read("AMPR?")
        
    def get_frequency(self):
        self.read("FREQ?")
        
