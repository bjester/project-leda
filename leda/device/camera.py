import picamera

MAX_WIDTH = 2592
MAX_HEIGHT = 1944


class Camera:
    """Project Ledas camera object"""

    def __init__(self, path, debug_obj):
        """Init resources and attach interval for recurring capture"""
        self.name = [path, None, ".jpg"]
        self.cam = picamera.PiCamera()
        self.cam.resolution = (MAX_WIDTH, MAX_HEIGHT)
        self.debug = debug_obj

    def capture(self, timestamp):
        """Take and store a picture"""
        self.name[1] = str(timestamp)
        self.debug.write('Camera: starting capture')
        self.cam.capture(''.join(self.name))
        self.debug.write('Camera: capture complete')
