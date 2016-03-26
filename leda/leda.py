import threading
import time
import signal


class Leda:
    """Handles Timing, data capture and logging"""

    def __init__(self, camera_obj, cam_period, uart_obj, serial_period, logger_obj, debug_obj):

        # assign capture periods
        self.cam = camera_obj
        self.cam_period = cam_period

        self.uart = uart_obj
        self.serial_period = serial_period

        self.log = logger_obj
        self.log.open()

        self.debug = debug_obj
        self.debug.open()

        self.kill_now = False

        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True

    def log_data(self, timestamp):
        self.debug.write("Logging data")
        # get sensor data from uart
        sensor_data = self.uart.capture()

        if sensor_data == False:
            self.uart.reset()
            self.debug.write("Bad data from daughter board")
        else:
            self.log.append(sensor_data, timestamp)
            self.debug.write("Daughter board data captured")

    def take_picture(self, time):
        self.debug.write("Taking picture")
        self.cam.capture(time)

    # requires tasks to finish in their allotted time
    def infinite_loop(self):
        self.debug.write("Successfully launched")
        wait = 4
        tick = 0
        while True:

            if self.kill_now:
                self.debug.write("Quitting")
                self.log.close()
                self.uart.close()
                self.debug.close()
                break

            # monotonic clock will not change as system time changes
            begin = time.clock_gettime(time.CLOCK_MONOTONIC)
            # system time can be converted to date/time stamp
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
