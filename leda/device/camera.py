import picamera
import device

MAX_WIDTH=2592
MAX_HEIGHT=1944

class Camera(device.Device):
    """Project Ledas camera object"""
    cam = picamera.PiCamera()
        

    # __init__(self, extraParams) acts like a constructor but this is a normal function
    def begin(self):
        """Init resources and attach interval for recurring capture"""
        self.cam.resolution = (MAX_WIDTH, MAX_HEIGHT)
        pass
    
    def capture(self):
        """Take and store a picture"""
        self.cam.capture('/home/pi/image.jpg')
        return

    def end(self):
        """If necessary, deallocate resources"""
        pass
