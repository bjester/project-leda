from time import sleep
import picamera
from device import Device



WIDTH=2592
HEIGHT=1944

class Camera(Device):
    """Project Ledas camera object"""

    # __init__(self, extraParams) acts like a constructor but this is a normal function
    def init(self, time):
        """Init resources and attach interval for recurring capture"""
        pass
    
    def capture():
        """Take and store a picture"""
        with picamera.PiCamera() as camera:
            camera.resolution = (WIDTH,HEIGHT)
            camera.start_preview()
            camera.capture('/home/pi/image.jpg')
            camera.stop_preview()
        print("wierd, print calls need to look like this")
        return "this is a test"

    def end():
        """If necessary, deallocate resources"""
        pass
    # Currently, a picamera object is created and destroyed every time a 
    #  pic is taken.  Too much overhead?
