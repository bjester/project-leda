#!/usr/bin/python
from leda import leda
import os






#Timeouts for measurements  (Configure with care, please)
cam_period = 5                 # "fairly often"
serial_period= 1                # twi serial
#serial_path = "/dev/sensors"   # device (in /dev directory)
#serial_path = "/dev/ttyACM1"       #   CHANGE BACK TO ABOVE LINE 
serial_path = "/dev/ttyUSB0"        # for USB mini to A adapter
baud = 38400                    # twi serial baud rate
serial_timeout = 1               # max time to wait for serial response  





#########################################################
if __name__ == "__main__":
    os.system("sudo killall -11 gpsd")
    os.system("sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.pid")
    t = leda.Leda(cam_period, 
              serial_period,
              serial_path,
              baud,
              serial_timeout)

    t.start() #launch the platform

