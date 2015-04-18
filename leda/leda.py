import zope.event
import time
from device import camera, uartSerial# jGps, radio, twiSerial, piGps, thermo
from data import logger
from event import capture_image
#import threading as th #Just to reduce horizontal width of code.


fairly_often = 1


class Leda:
    """Handles Project Leda system logic"""

    def __init__(self, cam_period, serial_period, serial_path, baudrate):
        self.serial_period      = serial_period 
        self.cam_period         = cam_period
        self.log             = logger.Logger("leda_log.txt") # needs to update each run 
        self.ledaCam         = camera.Camera()
        #self.ledaSerial      = twiSerial.TwiSerial(serial_path, baudrate, serial_period)
        #self.ledaGps         = jGps.PiGps("/dev/ttyUSB0", 4800, fairly_often)  # /dev/jGps ??  moved to daughter board
        #self.ledaRadio       = radio.Radio() #moved to proprietary module
        #self.CAM_ALTITUDE    = cam_altitude #take pics above this altitude

    def start(self):
        '''Init data logger, camera if necessary.'''
        # Write in the logger's labels as a introductory row- call this after header is written!
        #self.log.record(["TimeStamp", "Temperature1", "Temperature2", "Humidity", "Pressure", "Altitude", "Longitude", "Latitude"]); #not needed for writing binary files
        zope.event.append(self.handle)

        captureEv = capture_image.CaptureEvent('Hello!')
        zope.event.notify(captureEv)

        pass

        #result.append(GPS data here)
        while True:
            # Don't have altitude data, schedule occasional captures
            # Event system??
            #self.log.record(self.ledaSerial.capture())
            self.ledaCam.capture()
            time.sleep(self.cam_period)

    def handle(self, event):
        event.trigger()