#!/usr/bin/python
from leda import leda






#Timeouts for measurements  (Configure with care, please)
gps_timeout = 8                # "often"
cam_timeout = 15                # "fairly often"
thermo_timeout = 0.75           # exactly 750 ms
radio_timeout = gps_timeout     # as often as "often"
serial_timeout = 0.5            # twi serial
serial_path = "/dev/sensors"    # device (in /dev directory)
baud = 38400                    # twi serial baud rate
cam_altitude = 50000            # altitude that camera begins taking pictures





#########################################################
t = leda.Leda(gps_timeout, 
              cam_timeout, 
              thermo_timeout, 
              radio_timeout, 
              serial_timeout,
              serial_path,
              baud,
              cam_altitude)

t.start()

