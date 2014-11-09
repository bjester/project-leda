from device import camera, position, thermo
from data import logger
import time
import threading as th #Just to reduce horizontal width of code.

#Replace place holders (half-second) when interval is decided upon
#Thermometer = 750 milliseconds
#GPS  = "often"
#cams = "fairly often at high altitudes"
placeholder = 0.5

def update(device, interval):
#Intended for one thread per device capture functions.
    while True:     #WIP: while (not stop_condition) - 
                    #think about what to do about condition
                    #however only cams will need a stop condition (alt too low)
        device.capture()
        time.sleep(interval)
    #Otherwise, don't do anything.
    return

class Leda:
    """Handles Project Leda system logic"""
    def __init__(self):
        self.log        = logger.Logger("leda_log.txt")
        self.ledaCam    = camera.Camera()
        self.ledaGPS    = position.GPS(self.log)
        self.ledaThermo = thermo.Thermo()
        #Create the threads per device - interval is placeholder for now.
        self.cam_thread    = th.Thread(target = update, 
                                         args = (self.ledaCam, placeholder))
        self.gps_thread    = th.Thread(target = update, 
                                         args = (self.ledaGPS, placeholder))
        self.thermo_thread = th.Thread(target = update, 
                                         args = (self.ledaThermo, 0.75))

    def scheduler(self):
        self.gps_thread.start()
        self.thermo_thread.start()
        while True:
        #WIP: Have cams active only when the altitude is high enough
            pass
        pass

    def test(self):
        self.ledaCam.capture()
        print("testing; picture taken")
