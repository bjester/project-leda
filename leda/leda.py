from leda.device import camera
from leda.device import position

class Leda:
    """Handles Project Leda system logic"""
    def __init__(self):
        self.ledaCam = camera.Camera()
        self.ledaGPS = position.GPS()

    def test(self):
        self.ledaCam.capture()
        print("testing; picture taken")

