import datetime
import time
import picamera

MAX_WIDTH=2592
MAX_HEIGHT=1944

class Camera(): 
    """Project Ledas camera object"""
        

    def __init__(self, fileName):
        """Init resources and attach interval for recurring capture"""
        self.picNo = 0
        self.fileName = fileName
        self.cam = picamera.PiCamera()
        self.cam.resolution = (MAX_WIDTH, MAX_HEIGHT)

    def open(self):
        """Allocate resources as necessary"""
        self.cam.start_preview()

    def capture(self, timeStamp):
        """Take and store a picture"""
        name = self.fileName + " " + timeStamp.strftime("%Y-%m-%d %H:%M:%S") + " " + str(self.picNo)+ ".jpg"
        self.cam.capture(name)
        picNo += 1


    def close(self):
        """Deallocate resources as necessary"""
        self.cam.stop_preview()


#cam = Camera("test")
#cam.open()
#cam.capture(datetime.datetime.now())
#cam.capture(datetime.datetime.now())
#cam.capture(datetime.datetime.now())
#cam.close()

