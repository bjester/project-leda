#!/usr/bin/python3
import os
import time
import sys
from argparse import ArgumentParser

from leda import leda, factory, debug

print("Python version " + sys.version)

# RPi cam
cam_period = 5                      # in seconds

# Daughter (sensor) board over twi
twi_period = 1                      # in seconds
twi_path = "/dev/ttyACM0"           # db appears here by default
twi_baud = 38400
twi_timeout = 1                      # in seconds

gps_host = 'localhost'
gps_port = '2947'

parser = ArgumentParser()
parser.add_argument('--debug', dest='debug', action='store_true')
parser.set_defaults(debug=False)
args = parser.parse_args()

#########################################################
# ensure only one instance of Project Leda runs at once
if __name__ == "__main__":

    # create directory for this run 
    output_dir = "/home/pi/project-leda/Deployment_" + time.asctime(time.localtime()).replace(' ', '_').replace(':', '') + "/"
    output_pic_dir = output_dir + "pictures/"
    os.mkdir(output_dir)
    os.mkdir(output_pic_dir)

    debugger = debug.Logger(output_dir, args.debug)
    leda_factory = factory.Factory(debugger)

    # init project leda
    projectLeda = leda.Leda(
                    leda_factory.build_camera(output_pic_dir),
                    cam_period,
                    leda_factory.build_uart(twi_path, twi_baud, twi_timeout),
                    twi_period,
                    leda_factory.build_gps(gps_host, gps_port),
                    leda_factory.build_logger(output_dir),
                    debugger)

    # launch the system
    print("Launching Leda")
    projectLeda.infinite_loop() 

