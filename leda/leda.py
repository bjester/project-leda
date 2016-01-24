import time
import picamera
from device import camera,uart #uart requires python2.7
from data import logger





class Leda:
    """Handles Timing, data capture and logging"""

    def __init__(self, log_path, cam_period, image_path, serial_period, serial_path, baudrate, serial_timeout):
        # assign capture periods
        self.cam              = camera.Camera(image_path)
        self.cam_period       = cam_period
        self.serial_period    = serial_period 
        # initialize devices
        self.log              = logger.Logger(log_path)
        self.log.open()
        self.uart             = uart.Uart(serial_path, baudrate, serial_timeout)


    def start(self):
        while True:
            begin= time.time()
            #send signal to take picture
            #send signal to get sensor data

            #timestamp is beginning of data capture
            #get sensor data from uart (WIP)
            #sensorData = self.uart.capture()
            #if sensorData == False:
            #   self.uart.reset()
            #   print "Bad data from daughter board"
            #else:
            #   self.log.append(sensorData, begin)
            #    print "data captured"

            self.cam.capture(begin)

            delta = time.time() - begin
            if self.serial_period > delta:
                time.sleep(self.serial_period - delta) 


        
