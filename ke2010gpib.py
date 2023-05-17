import pyvisa
import re

#Communication with Ke2010 Multimeter is enabled by PyVisa package over a GPIB Interface 
#using a combination of IEEE 488 commands as well as additional commands detailed in the device manual

class Ke2010():

    def __init__(self,target_port):
        #PyVisa handling of device
        rm = pyvisa.ResourceManager()
        self.device = rm.open_resource(target_port)
        self.device.write("*RST")

    def check_connection(self):
        return self.device.query("*IDN?")

    def read_voltage(self):
        #Apply averaging filter (currently disabled)
        #self.device.write('SENSe:VOLT:DC:AVER:COUNt 2')
        #self.device.write('SENSe:VOLT:DC:AVER:STATe ON')
        #Get Query form device, this is formatted as a sting like "10.0E-3\n"
        tmp = self.device.query("READ?")
        #Subract linebreak
        tmp = re.sub("\n","",tmp)
        #Transform cleaned output into a proper floating point number (i.e. "10.0E-3" -> 0.01)
        tmparr = re.split("E",tmp)
        tmp = float(tmparr[0])*10**(int(tmparr[1]))
        return tmp

    #!!Implement functionality to read unit
    def read_unit(self):
        return "arb.u."
