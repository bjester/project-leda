import picamera

MAX_WIDTH=2592
MAX_HEIGHT=1944

class Camera(): 
    """Project Ledas camera object"""
        

    def __init__(self, path):
        """Init resources and attach interval for recurring capture"""
        self.name = [path, None, ".jpg"]
        self.cam = picamera.PiCamera()
        self.cam.resolution = (MAX_WIDTH, MAX_HEIGHT)

    def capture(self, timeStamp):
        """Take and store a picture"""
        self.name[1] = str(timeStamp)
        self.cam.capture(''.join(self.name))

