from device import camera, position, thermo
from data import logger

class Leda:
    """Handles Project Leda system logic"""
    def __init__(self):
        self.log = logger.Logger("leda_log.txt")
        self.ledaCam = camera.Camera()
        self.ledaGPS = position.GPS(self.log)
        self.ledaThermo = thermo.Thermo()
    def test(self):
        self.ledaCam.capture()
        print("testing; picture taken")
