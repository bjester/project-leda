import time
import zope.event
import picamera
from device import uart #uart requires python2.7
from data import logger
#from event import capture_image


fairly_often = 1000



class Leda:
    """Handles Timing, data capture and logging"""

    def __init__(self, cam_period, image_path, serial_period, serial_path, baudrate, serial_timeout):
        # assign capture periods
        self.cam_period      = cam_period
        self.serial_period   = serial_period 
        # initialize devices
        self.ledaCam         = Camera(image_path)
        self.log             = logger.Logger("leda_log")
        self.ledaSerial      = uartSerial.UartSerial(serial_path, baudrate, serial_timeout)


    def start(self):
        while True:
            time_intial = time.process_time()
            #get sensor data from uart (WIP)
            self.log.append(ledaSerial.caputure())
            #catch camera finished capture event.... i think
            ledaCam.capture()
            delta = time.process_time() - time_initial
            if fairly_often > delta:
                time.sleep(fairly_often - delta)


    #def handle(self, event):
    #    event.trigger()
