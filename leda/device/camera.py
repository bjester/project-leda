from time import sleep
import picamera

WIDTH=2592
HEIGHT=1944


with picamera.PiCamera() as camera:
    camera.resolution = (WIDTH,HEIGHT)
    camera.start_preview()
    camera.capture('/home/pi/image.jpg')
    camera.stop_preview()


#from leda.device import device
#class Camera(device.Device):   # Camera inherits from device.Device object??
#    pass
