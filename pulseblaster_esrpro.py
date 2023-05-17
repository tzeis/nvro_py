from spinapi import *
import re
import ast

class PulseBlasterEsrpro():

    def __init__(self):
        #Initialization according to spinapi documentation
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
        #Program start in spinapi
        pb_start_programming(PULSE_PROGRAM)
        #Split program string by linebreaks
        lines = re.split("\n",program)
        #for-loop sequentially programming instructions from given lines
        for i in range(len(lines)):
            #TODO: remove unsafe eval and replace with ast.literal_eval using opcodes in pb programs
            #Reads an instruction line as list of python data from program string
            instr = ast.literal_eval(lines[i])
            #Passes the instruction to the PulseBlaster card
            pb_inst_pbonly(instr[0],instr[1],instr[2],instr[3])
        #Program stop in spinapi
        pb_stop_programming()

    def start(self):
        pb_reset()
        pb_start()

    def stop(self):
        pb_stop()

    def disconnect(self):
        pb_close()
