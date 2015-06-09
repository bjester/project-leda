import time
import picamera
from leda.device import device

MAX_WIDTH=2592
MAX_HEIGHT=1944

class Camera(): 
    """Project Ledas camera object"""
        

    def __init__(self, fileName):
        """Init resources and attach interval for recurring capture"""
        self.fileName = fileName
        self.cam = picamera.PiCamera()
        self.cam.resolution = (MAX_WIDTH, MAX_HEIGHT)
        self.cam.start_preview()

    def capture(self, timeStamp):
        """Take and store a picture"""
        name = self.fileName + " " + timeStamp + ".jpg"
        self.cam.capture(name)


    def close():
        """Deallocate resources as necessary"""
        self.cam.stop_preview()
