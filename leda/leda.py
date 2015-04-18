from device import camera, jGps, radio, twiSerial  # piGps, thermo
from data import logger
import time
import threading as th #Just to reduce horizontal width of code.


fairly_often = 1

def update(device, interval):
# Intended for one thread per device.
    time.sleep(interval)
    return device.capture()

class Leda:
    """Handles Project Leda system logic"""

    def __init__(self, gps_timeout, cam_timeout, radio_timeout, serial_timeout, serial_device, baudrate, cam_altitude):
        self.CAM_ALTITUDE    = cam_altitude
        self.cam_timeout     = cam_timeout
        self.log             = logger.Logger("leda_log.txt")
        self.ledaCam         = camera.Camera()
        self.ledaGps         = jGps.PiGps("/dev/ttyUSB0", 4800, fairly_often)  # /dev/jGps !!!!!!!!! make the change
        self.ledaRadio       = radio.Radio()
        self.ledaSerial      = twiSerial.TwiSerial(serial_device, baudrate, fairly_often)

    def start(self):
        '''Acquire information, unify data and log them.'''
        # P.S Above new plan made while Jeff is sleeping- for CSV coherence.
        # Write in the logger's labels as a introductory row- call this after header is written!
        self.log.record(["Pulse", "Tempurature", "Humidity", "Pressure", "Altitude", "Longitude", "Latitude", "Time"])

        #Acquire return values from these threads, append them together and record.
        result = self.ledaSerial.capture()

        #result.append(GPS data here)
        while True:
            # Have cams active only when the altitude is high enough.
            if self.ledaGps.get_altitude() > self.CAM_ALTITUDE:
                self.ledaCam.capture()
            time.sleep(self.cam_timeout)
            self.ledaRadio.transmit(self.ledaGps.get_position())

