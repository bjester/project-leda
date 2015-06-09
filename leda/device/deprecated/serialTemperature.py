"""" Using the DS1631 Digital Thermostat"""""
"Converts Temperature-to-digital Word in 750ms (max)"
"""Might need more configuring and stuff. I just wanted to make a module that produced a temperature in C"""
"""Using DS1631 thermometer (http://datasheets.maximintegrated.com/en/ds/DS1631-DS1731.pdf)"""
from leda.device import device
import serial

class SerialTemperature(device.Device):
    """Project Ledas Serial object"""


    # __init__(self, extraParams) acts like a constructor but this is a normal function
    #bus should be a SMBus initialized externally. I'd like to only have one instance of I2C shared by all the devices
    #address should be the thermometer's address on I2C
    def init(self, device_path, baud, tout)
        """Init resources and attach interval for recurring commands"""
        self.RECV_BYTES = 4
        self.device = device_path
        port = serial.Serial(device_path, baudrate=baud, timeout=tout)


    def capture(self):
        """Capture all daughter board sensor data"""
        port.write('t') #request outside temperature
        temp = port.read(self.RECV_BYTES) #get temp
        port.write('h')
        humidity = port.read(self.RECV_BYTES)
        port.write('p')
        pressure = port.read(self.RECV_BYTES)
        port.write('x')
        accel_x = port.read(self.RECV_BYTES)
        port.write('y')
        accel_y = port.read(self.RECV_BYTES)
        port.write('z')
        accel_z = port.read(self.RECV_BYTES)
        return (temp, humidity, pressure, accel_x, accel_y, accel_z)


    def end(self):
        """If necessary, deallocate resources"""
        port.close()
        pass
