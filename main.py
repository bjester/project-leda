#!/usr/bin/python3
##!/usr/local/bin/python3.5
from leda import leda
import os
import time

import sys
print("Python version " + sys.version)





# RPi cam
cam_period = 5                      #in seconds

# Daughter (sensor) board over twi
twi_period = 1                      #in seconds
#twi_path = "/dev/leda-db"           #db configed to appear here
twi_path = "/dev/ttyACM0"           #db appears here by default
twi_baud = 38400
twi_timeout= 1                      #in seconds





#########################################################
# ensure only one instance of Project Leda runs at once
if __name__ == "__main__":


    # create directory for this run 
    newDir = "/home/pi/project-leda/Deployment " + time.asctime(time.localtime()) + "/"
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
    print("Launching Leda")
    projectLeda.infinite_loop() 

