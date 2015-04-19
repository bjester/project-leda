#!/bin/python3
#Functions to be used by Leda scheduler
import serial

# (Serial object, message)
# Specifically, this project expects message to be:
#   {"S\r\n", "A\r\n"}
def send_to_board(serialobj, msg):
    if serialobj.isOpen() != True:
        serialobj.open()
    serialobj.write(msg)

# (Serial object, logger)
def read_measurement(serialobj, logger):
    if serialobj.isOpen() != True:
        serialobj.open()
    bits = serialobj.read(10)
    logger.record(bits)
    pass

#Testing Area.
testdevice = serial.Serial("/dev/ttyUSB0", baudrate = 38400)
print send_to_board(testdevice, "S\r\n")
# wait for 'A\r\n' at least 800ms
print send_to_board(testdevice, "A\r\n")
# read data (stop read after '\r\n')
