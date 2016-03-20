import threading
import time

class Leda:
    """Handles Timing, data capture and logging"""

    def __init__(self, camera_obj, cam_period, uart_obj, serial_period, logger_obj):

        # assign capture periods
        self.cam = camera_obj
        self.cam_period = cam_period

        self.uart = uart_obj
        self.serial_period = serial_period

        self.log = logger_obj
        self.log.open()


    def log_data(self, timestamp):
        print("LoggingData")
        #get sensor data from uart
        sensorData = self.uart.capture()

        if sensorData == False:
            self.uart.reset()
            print("Bad data from daughter board")
        else:
            self.log.append(sensorData, timestamp)
            print("data captured")


    def take_picture(self, time):
        print("TakingPicture")
        self.cam.capture(time)


    #requires tasks to finish in their allotted time
    def infinite_loop(self):
        print("Successfully Launched")
        wait = 4
        tick = 0
        while True:
            #monotonic clock will not change as sytem time changes
            begin = time.clock_gettime(time.CLOCK_MONOTONIC)
            #system time can be converted to date/time stamp
            stamp = time.time()
            t1 = threading.Thread(target=self.log_data, args=(stamp,))
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
