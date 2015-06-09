import zope.event
#import asyncio # requires python 3.4+
# uartSerial requires python 2.7
from device import camera, uartSerial #jGps, radio, twiSerial, piGps, thermo
from data import logger
from event import capture_image
#import threading as th #Just to reduce horizontal width of code.


fairly_often = 1

# Send event for camera (begin image capture), receive sensor data (1 action)

class Leda:
    """Handles Project Leda system logic"""

    def __init__(self, cam_period, serial_period, serial_path, baudrate, serial_timeout):
        self.ledaCam         = camera.Camera()
        #self.ledaCam.begin()

        self.log             = logger.Logger("leda_log")
        self.log.begin()

        self.serial_period   = serial_period 
        self.cam_period      = cam_period
        self.ledaSerial      = uartSerial.UartSerial(serial_path, baudrate, serial_timeout)
        #self.ledaSerial.begin()

        #self.ledaSerial      = twiSerial.TwiSerial(serial_path, baudrate, serial_period)
        #self.ledaGps         = jGps.PiGps("/dev/ttyUSB0", 4800, fairly_often)  # /dev/jGps ??  moved to daughter board
        #self.ledaRadio       = radio.Radio() #moved to proprietary module
        #self.CAM_ALTITUDE    = cam_altitude #take pics above this altitude

    def start(self):
        while True:
            time_intial = time.process_time()
            #Fire off capture event
            #receive sensor data
            #uart WIP
            #catch camera finished capture event.... i think
            delta = time.process_time() - time_initial
            if fairly_often > delta:
                time.sleep(fairly_often - delta)


    def handle(self, event):
        event.trigger()
