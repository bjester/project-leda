from time import sleep
import picamera
from leda.device import device

MAX_WIDTH=2592
MAX_HEIGHT=1944

class Camera(device.Device):
    """Project Ledas camera object"""

    # __init__(self, extraParams) acts like a constructor but this is a normal function
    def begin(self, time):
        """Init resources and attach interval for recurring capture"""
        pass
    
    def capture(self):
        """Take and store a picture"""
        with picamera.PiCamera() as camera:
            camera.resolution = (MAX_WIDTH, MAX_HEIGHT)
            camera.start_preview()
            camera.capture('/home/pi/image.jpg')
            camera.stop_preview()
        return

    def end(self):
        """If necessary, deallocate resources"""
        pass
    # Currently, a picamera object is created and destroyed every time a 
    #  pic is taken.  Too much overhead?
