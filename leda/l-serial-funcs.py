#Functions to be used by Leda scheduler
import serial

# (Serial object, message)
# Specifically, this project expects message to be:
#   {"S\r\n", "A\r\n"}
def send_to_board(serialobj, msg):
    if serialobj.isOpen() != True:
        serialobj.open()
    serialobj.write(msg)
    pass

# (Serial object, logger)
def read_measurement(serialobj, logger):
    #Data format is:
    # 16 bit - Tempurature DS361
    # 16 bit - Pressure ANPxS100AP
    # 16 bit - Pressure 2 MPx4411SVCGU
    # 16 bit - Humidity HIH8120
    # 16 bit - Temperature
    # 80 bits total - closed by \r\n
    if serialobj.isOpen() != True:
        serialobj.open()
    bits = serialobj.read(10)
    logger.record(bits)
    pass

#Testing Area.
testdevice = serial.Serial("/dev/ttyACM1", baudrate = 38400)
print send_to_board(testdevice, "S\r\n")
print send_to_board(testdevice, "A\r\n")