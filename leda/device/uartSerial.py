"""" Daughter Board - Pi serial interface"""""
import device
import serial
import time
import io

class UartSerial(device.Device):
    """Project Ledas Serial object"""


    def __init__(self, device_path, baud, tout):
        """Init resources and attach interval for recurring commands"""
        self.device = device_path
        self.ser = serial.Serial(device_path, baudrate=baud, timeout=tout)
        self.port = io.TextIOWrapper(io.BufferedRWPair(self.ser, self.ser))


    def capture(self):
        """Capture all daughter board sensor data"""
        # request 'S\r\n'
        self.port.write(unicode("S\r\n"))
        # wait for Ack that data is ready  (receive 'A\r\n')
        ack = self.port.read(3);
        if ack == "A\r\n" :
            return false # received bad data
        print("Ack received")
        # request the data
        self.port.write(unicode("R\r\n"))
        time.sleep(1)
        # read the data
        return self.port.readline()

    def end(self):
        """If necessary, deallocate resources"""
        self.port.close()

