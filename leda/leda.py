from datetime import datetime
import time
import zope.event
import picamera
from device import camera,uart #uart requires python2.7
from data import logger
#from event import capture_image

fairly_often = 1000



class Leda:
    """Handles Timing, data capture and logging"""

    def __init__(self, log_name, cam_period, image_path, serial_period, serial_path, baudrate, serial_timeout):
        # assign capture periods
        self.cam_period       = cam_period
        self.serial_period    = serial_period 
        # initialize devices
        #self.cam              = camera.Camera(image_path)
        self.log              = logger.Logger(log_name)
        self.log.open()
        self.uart             = uart.Uart(serial_path, baudrate, serial_timeout)


    def start(self):
        fairlyOftenInSeconds = fairly_often/1000
        while True:
            time_initial = time.time()
            self.captureAll()

            delta = time.time() - time_initial
            if fairlyOftenInSeconds > delta:
                time.sleep(fairlyOftenInSeconds - delta) 


    def captureAll(self):
        #timestamp is beginning of data capture
        #!!Some delay possible
        now = datetime.now() 
        #ISSUE:  must launch data capture and camera NOW to ensure validity of time stamp
        #Soln:  threads?  event library?

        #get sensor data from uart (WIP)
        sensorData = self.uart.capture()
        if sensorData == False:
            self.uart.reset()
            print "Bad data from daughter board"
        else:
            self.log.append(sensorData, now)
        #catch camera finished capture event.... i think
        #ledaCam.capture(now)


    #def handle(self, event):
    #    event.trigger()
