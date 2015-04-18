from device import camera, jGps, radio, twiSerial  # piGps, thermo
from data import logger
import time
import threading as th #Just to reduce horizontal width of code.


fairly_often = 1

def update(device, interval):
# Intended for one thread per device.
    time.sleep(interval)
    return device.capture()

class Leda:
    """Handles Project Leda system logic"""

    def __init__(self, se, serial_device, baudrate):
        self.sleep_time      = sleep_time 
        self.log             = logger.Logger("leda_log.txt")
        self.ledaCam         = camera.Camera()
        self.ledaSerial      = twiSerial.TwiSerial(serial_device, baudrate, fairly_often)
        #self.ledaGps         = jGps.PiGps("/dev/ttyUSB0", 4800, fairly_often)  # /dev/jGps ??  moved to daughter board
        #self.ledaRadio       = radio.Radio() #moved to proprietary module
        #self.CAM_ALTITUDE    = cam_altitude #take pics above this altitude

    def start(self):
        '''Init data logger, camera if necessary.'''
        # Write in the logger's labels as a introductory row- call this after header is written!
        #self.log.record(["TimeStamp", "Temperature1", "Temperature2", "Humidity", "Pressure", "Altitude", "Longitude", "Latitude"]); #not needed for writing binary files
        pass

        #result.append(GPS data here)
        while True:
            # Don't have altitude data, schedule occasional captures
            # Event system??
            self.log.record(self.ledaSerial.capture())
            self.ledaCam.capture()
            time.sleep(self.cam_timeout)

