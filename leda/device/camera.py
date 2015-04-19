import time
import picamera
from leda.device import device

MAX_WIDTH=2592
MAX_HEIGHT=1944

class Camera(): #device.Device):
    """Project Ledas camera object"""
    fileName = "/home/pi/pics/image"
    n_picture = 0  # number of pictures
        

    def __init__(self):
        """Init resources and attach interval for recurring capture"""

    def __enter__(self):
        """Calling this ensures that __exit__() is called on object destruction"""
        pass

    def capture(self):
        """Take and store a picture"""
        with picamera.PiCamera() as self.cam:
            self.cam.resolution = (MAX_WIDTH, MAX_HEIGHT)
            name = self.fileName + " " + time.asctime(time.localtime()) + ".jpg"
            self.cam.capture(name)
            self.n_picture += 1  # because ++n_picture is Not increment

    def __exit__(self, type, value, traceback):
        """If necessary, deallocate resources"""
        pass

