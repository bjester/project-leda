from leda.device import camera
from leda.device import gps

class Leda:
    """Handles Project Leda system logic"""
    def __init__(self):
        self.camera = camera.Camera()
        self.gps = gps.GPS()
