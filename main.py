#!/usr/bin/python
from leda import leda
import os
import time





# RPi cam
cam_period = 5                      #in seconds

# Daughter (sensor) board over twi
twi_period = 1                      #in seconds
twi_path = "/dev/leda-db"           #db configed to appear here
twi_baud = 38400
twi_timeout= 1                      #in seconds





#########################################################
# ensure only one instance of Project Leda runs at once
if __name__ == "__main__":

    # setup GPS for time if no RTC configured 
    #os.system("sudo killall -11 gpsd")
    #os.system("sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.pid")

    
    # create directory for this run 
    newDir = "Deployment " + time.asctime(time.localtime()) + "/"
    newPicDir = newDir + "pictures/"
    os.mkdir(newDir)
    os.mkdir(newPicDir)

    # init project leda
    projectLeda = leda.Leda(
                  newDir,
                  cam_period,
                  newPicDir,
                  twi_period,
                  twi_path,
                  twi_baud,
                  twi_timeout)

    # launch the system
    projectLeda.start() 

