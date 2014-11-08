import picamera


MAX_WIDTH=2592
MAX_HEIGHT=1944

print("Press enter to exit")
cam = picamera.PiCamera()
cam.start_preview()
input("... waiting ... ")
cam.stop_preview()


