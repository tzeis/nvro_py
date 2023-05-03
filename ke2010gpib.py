import pyvisa
import re

class Ke2010():

    def __init__(self,target_port):
        rm = pyvisa.ResourceManager()
        #Opens and Resets Device
        self.device = rm.open_resource(target_port)
        self.device.write("*RST")

    def check_connection(self):
        return self.device.query("*IDN?")

    def read_voltage(self):
        #Apply averaging filter
        #self.device.write('SENSe:VOLT:DC:AVER:COUNt 2')
        #self.device.write('SENSe:VOLT:DC:AVER:STATe ON')
        #Process output to ordinary float
        tmp = self.device.query("READ?")
        #Subract string terminator
        tmp = re.sub("\n","",tmp)
        tmparr = re.split("E",tmp)
        tmp = float(tmparr[0])*10**(int(tmparr[1]))
        return tmp

    #Implementieren
    def read_unit(self):
        return "arb.u."
