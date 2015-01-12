from device import camera, position, thermo
from data import logger
import time
import threading as th #Just to reduce horizontal width of code.

#Replace place holders (half-second) when interval is decided upon
gpsInterval  = 1                # "often"
camInterval = 2                 # "fairly often"
thermoInterval = 0.75           # exactly 750 ms
radioInterval = gpsInterval     # as often as "often"
serialInterval = 5              # \o.O/
placeholder = 1                 # Must replace this!!!!


def update(logger, device, interval):
# Intended for one thread per device capture->logger
    while True:     # infinite loop 
        logger.record(device.capture())
        time.sleep(interval)
    return


class Leda:
    """Handles Project Leda system logic"""
    def __init__(self, serial_device, baudrate, serial_timeout):
        self.log        = logger.Logger("leda_log.txt")
        self.ledaCam    = camera.Camera()
        self.ledaGPS    = position.GPS(self.log)
        self.ledaRadio = radio.Radio()
        self.ledaThermo = thermo.Thermo()
        self.ledaSerial = serial.Serial(serial_device, baudrate, serial_time)
        #Create the threads for devices using logger 
        self.gps_thread    = th.Thread(target = update, 
                                         args = (self.log, self.ledaGPS, placeholder))
        self.thermo_thread = th.Thread(target = update, 
                                         args = (self.log, self.ledaThermo, thermoInterval))
        self.serial_thread = th.Thread(target = update, 
                                         args = (self.log, self.ledaSerial, serialInterval))


    def begin(self):
        self.gps_thread.start()
        self.thermo_thread.start()
        self.serial_thread.start()
        while True:  #infinite loop
            # Have cams active only when the altitude is high enough
            if self.ledaGPS.get_position() > CAM_ALTITUDE:
                self.ledaCam.capture()
            time.sleep(camInterval) 
            self.ledaRadio.transmit(self.ledaGPS.get_position())

