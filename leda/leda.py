from device import camera, jGps, radio, twiSerial  # piGps, thermo
from data import logger
import time
import threading as th #Just to reduce horizontal width of code.



def update(logger, device, interval):
# Intended for one thread per device capture->logger
    while True:     # infinite loop 
        logger.record(device.capture())
        time.sleep(interval)
    return


class Leda:
    """Handles Project Leda system logic"""

    def __init__(self, gps_timeout, cam_timeout, thermo_timeout, radio_timeout, serial_timeout, serial_device, baudrate, cam_altitude):
        self.CAM_ALTITUDE    = cam_altitude
        self.cam_timeout     = cam_timeout
        self.log             = logger.Logger("leda_log.txt")
        self.ledaCam         = camera.Camera()
        self.ledaGps         = jGps.PiGps("/dev/ttyUSB0", 4800, gps_timeout)  # /dev/jGps !!!!!!!!! make the change!
        #self.ledaGps         = piGps.PiGps()
        self.ledaRadio       = radio.Radio()
        #self.ledaThermo      = thermo.Thermo()  # now handled by arduino
        self.ledaSerial      = twiSerial.TwiSerial(serial_device, baudrate, serial_timeout)
        #Create the threads for devices using logger 
        self.gps_thread    = th.Thread(target = update, 
                                         args = (self.log, self.ledaGps, gps_timeout))
        #self.thermo_thread = th.Thread(target = update, 
        #                                 args = (self.log, self.ledaThermo, thermo_timeout))
        self.serial_thread = th.Thread(target = update, 
                                         args = (self.log, self.ledaSerial, serial_timeout))


    def start(self):
        self.gps_thread.start()
        #self.thermo_thread.start()
        self.serial_thread.start()
        while True:  #infinite loop
            # Have cams active only when the altitude is high enough
            if self.ledaGps.get_altitude() > self.CAM_ALTITUDE:
                self.ledaCam.capture()
            time.sleep(self.cam_timeout) 
            self.ledaRadio.transmit(self.ledaGps.get_position())

