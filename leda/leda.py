import threading
import time
import picamera
from .device import camera, uart
from .data import logger


class Leda:
    """Handles Timing, data capture and logging"""

    def __init__(self, log_path, cam_period, image_path, serial_period, serial_path, baudrate, serial_timeout):
        # assign capture periods
        self.cam= camera.Camera(image_path)
        self.cam_period= cam_period
        self.serial_period= serial_period 
        # initialize devices
        self.log= logger.Logger(log_path)
        self.log.open()
        self.uart= uart.Uart(serial_path, baudrate, serial_timeout)


    def log_data(self):
        print("LoggingData")
        print("Not Yet Implemented")
        #get sensor data from uart (WIP)
        #sensorData = self.uart.capture()
        #if sensorData == False:
        #    self.uart.reset()
        #    print("Bad data from daughter board")
        #else:
        #    self.log.append(sensorData, begin)
        #    print("data captured")

    def take_picture(self, time):
        print("TakingPicture")
        self.cam.capture(time)





    #requires tasks to finish in their allotted time
    def infinite_loop(self):
        print("Successfully Launched")
        wait = 4
        tick = 0
        while True:
            begin = time.clock_gettime(time.CLOCK_MONOTONIC)
            t1 = threading.Thread(target=self.log_data)
            t1.start()
            if tick >= wait:
                tick = 0
                t2 = threading.Thread(target=self.take_picture, args=(begin,))
                t2.start()
            else:
                tick = tick + 1
            delta = time.clock_gettime(time.CLOCK_MONOTONIC) - begin
            if self.serial_period > delta:
                time.sleep(self.serial_period - delta) 

