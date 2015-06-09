"""" Using PI serial over USB"""""
"Converts Temperature-to-digital Word in 750ms (max)"
"""Might need more configuring and stuff. I just wanted to make a module that produced a temperature in C"""
"""Using DS1631 thermometer (http://datasheets.maximintegrated.com/en/ds/DS1631-DS1731.pdf)"""
import serial
from leda.device import device


class TwiSerial(device.Device):
    """Project Ledas Serial object"""


    # __init__(self, extraParams) acts like a constructor but this is a normal function
    #bus should be a SMBus initialized externally. I'd like to only have one instance of I2C shared by all the devices
    #address should be the thermometer's address on I2C
    def __init__(self, device_path, baud, tout):
        self.RECV_BYTES = 4
        self.device = device_path
        self.port = serial.Serial(device_path, baudrate=baud, timeout=tout)

    def __enter__(self):
        """Init resources and attach interval for recurring commands"""
        pass

    def capture(self):
        """Capture all daughter board sensor data"""
        self.port.write('t') #request outside temperature
        temp = self.port.read(self.RECV_BYTES) #get temp
        self.port.write('h')
        humidity = self.port.read(self.RECV_BYTES)
        self.port.write('p')
        pressure = self.port.read(self.RECV_BYTES)
        self.port.write('x')
        accel_x = self.port.read(self.RECV_BYTES)
        self.port.write('y')
        accel_y = self.port.read(self.RECV_BYTES)
        self.port.write('z')
        accel_z = self.port.read(self.RECV_BYTES)
        return (temp, humidity, pressure, accel_x, accel_y, accel_z)

    def __exit__(self):
        """If necessary, deallocate resources"""
        self.port.close()
        pass
