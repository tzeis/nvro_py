import random

#A virtual Readout device to simulate Input for debugging purposes

class Vmvirtual():

    def __init__(self,target_port):
        self.port  = target_port

    def check_connection(self):
        #Pretend to be connected to passed port
        return "Virtual Signal Generator at" +str(self.port)

    def read_voltage(self):
        #Returns a random float between 0 and 1 as readout
        return random.random()

    def read_unit(self):
        #Unit to make it obvious that this is not a real device
        return "made up unit measuring nothing"
