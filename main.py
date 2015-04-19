#!/usr/bin/python
from leda import leda






#Timeouts for measurements  (Configure with care, please)
cam_period = 5                 # "fairly often"
serial_period= 1                # twi serial
#serial_path = "/dev/sensors"   # device (in /dev directory)
serial_path = "/dev/ttyACM1"       #   CHANGE BACK TO ABOVE LINE 
baud = 38400                    # twi serial baud rate
serial_timeout = 1               # max time to wait for serial response  





#########################################################
t = leda.Leda(cam_period, 
              serial_period,
              serial_path,
              baud,
              serial_timeout)

t.start()

