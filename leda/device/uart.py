"""" Daughter Board - Pi serial interface"""""
import device
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
        # request 'S\r\n'
        self.ser.write("S\n")
        # wait for Ack that data is ready  (receive 'A\r\n')
        ack = self.ser.readline();
        if ack == "A\n":
            return false # received bad data
        print("Ack received")
        # request the data
        self.ser.write("R\n")
        #time.sleep(1)
        # read the data
        result = []
        i = 0
        while True:
            temp = self.ser.readline() #need to remove line break
            #temp = (self.port.read(3)).strip() print(temp, i)
            result += temp
            i += 1
            if i > 5:
                break
            time.sleep(1)

    def end(self):
        """If necessary, deallocate resources"""
        self.port.close()

