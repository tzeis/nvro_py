import time

#A class to give a timer by acessing system time, not particularly useful but necessary to allow "hotswap" of system time with timer hardware 
class System_timer():

    def __init__(self):
        pass

    def get_time():
        return time.time()