#!/usr/bin/python
from leda import leda
import os






log_name = "leda_log"
#Timeouts for measurements  (Configure with care, please)
cam_period = 5000                 # "fairly often"
image_path = "/home/pi/pics/image"
serial_period= 1000                # twi serial
#serial_path = "/dev/sensors"   # device (in /dev directory)
#serial_path = "/dev/ttyACM1"       #   CHANGE BACK TO ABOVE LINE 
serial_path = "/dev/leda-db"        # for daughter (sensor) board
baud = 38400                    # twi serial baud rate
serial_timeout = 1000               # max time to wait for serial response  





#########################################################
#ensure only one instance of Project Leda runs at once
if __name__ == "__main__":
    os.system("sudo killall -11 gpsd")
    os.system("sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.pid")
    projectLeda = leda.Leda(
                  log_name,
                  cam_period,
                  image_path,
                  serial_period,
                  serial_path,
                  baud,
                  serial_timeout)

    projectLeda.start() #launch the platform

