from leda.device import camera
from leda.device import gps

class Leda:
    """Handles Project Leda system logic"""
    def __init__(self):
        self.ledaCam = camera.Camera()
        self.ledaGPS = gps.GPS()

    def test(self):
        self.ledaCam.capture()
        print("testing; picture taken")

