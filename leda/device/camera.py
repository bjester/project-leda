from time import sleep
import picamera

WIDTH=1280
HEIGHT=1024


with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.capture('~/image.jpg', format='jpg', resize=(WIDTH,HEIGHT))
    camera.stop_preview()


#from leda.device import device
#class Camera(device.Device):   # Camera inherits from device.Device object??
#    pass
