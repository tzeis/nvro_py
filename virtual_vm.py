import random

class Vmvirtual():

    def __init__(self,target_port):
        self.port  = target_port

    def check_connection(self):
        return "Virtual Signal Generator at" +str(self.port)

    def read_voltage(self):
        #Apply averaging filter
        #self.device.write('SENSe:VOLT:DC:AVER:COUNt 2')
        #self.device.write('SENSe:VOLT:DC:AVER:STATe ON')
        #Process output to ordinary float
        return random.random()

    #Implementieren
    def read_unit(self):
        return "made up unit"
