"""" Daughter Board - Pi serial interface"""""
import serial
import time
import io

class Uart:

    def __init__(self, device_path, baud, tout):
        """Init resources and attach interval for recurring commands"""
        self.device = device_path
        self.ser = serial.Serial(device_path, baudrate=baud, timeout=tout)
        self.ser.flushInput()


    def capture(self):
        """Capture all daughter board sensor data"""
        # request 'S\n'
        self.ser.write("S\n")
        # wait for Ack that data is ready  (receive 'A\n')
        ack = self.ser.readline();
        if ack == "A\n":
            return false # received bad data
        print("Ack received")
        # request the data
        self.ser.write("R\n")
        #time.sleep(1)
        # read the data
        return self.ser.readline() #need to remove line break

    def end(self):
        """If necessary, deallocate resources"""
        self.port.close()


#TEST AREA
uart = Uart("/dev/ttyACM0", 38400, 1000)
print uart.capture()

