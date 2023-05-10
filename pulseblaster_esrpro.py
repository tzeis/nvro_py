from spinapi import *
import re

class PulseBlasterEsrpro():

    def __init__(self):
        pb_init()
        pb_core_clock(500)

    def check_connection(self):
        return "Connected to PulseBlaster with Status" + str(pb_read_status())

    def is_running(self):
        status_string = str(pb_read_status())
        running_pattern = "..1{29}."
        if re.match(running_pattern,status_string) != None:
            return True
        else:
            return False

    def program(self,program):
        pb_start_programming(PULSE_PROGRAM)
        #Programmbeginn
        start = pb_inst_pbonly(0b000000000000000000000000,CONTINUE,0,200.0)
        pb_inst_pbonly(0b111111111111111111111111,BRANCH,start,200.0)
        #Programmende
        pb_stop_programming()

    def start(self):
        pb_reset()
        pb_start()

    def stop(self):
        pb_stop()

    def disconnect(self):
        pb_close()
