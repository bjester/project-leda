"""" Using the DS1631 Digital Thermostat"""""
"Converts Temperature-to-digital Word in 750ms (max)"
"""Might need more configuring and stuff. I just wanted to make a module that produced a temperature in C"""
"""Using DS1631 thermometer (http://datasheets.maximintegrated.com/en/ds/DS1631-DS1731.pdf)"""
from leda.device import device
import smbus

class Thermo(device.Device):
    """Project Ledas Thermostat object"""
    bus = None #http://www.prwatch.org/files/images/nuns_on_the_bus.jpg
    address = None
    #bus should be a SMBus initialized externally. I'd like to only have one instance of I2C shared by all the devices
    #address should be the thermometer's address on I2C
    def __init__(self, time, address, bus):
        self.bus = bus
        self.address = address
    
    def __enter__(self):
        """Init resources and attach interval for recurring capture"""
        pass
        
    def capture(self):
        """Capture temperature data"""
        temp = self.bus.read_word_data(self.address,0xAA) #0xAA is the command to read the temperature from the thermometer
        temp = (temp/256+temp*256)%65536 #swap endians (1 little 2 little 3 little endian...)
        if temp & 0x8000:
            temp = temp - 0x10000 #python thinks it's a 32 bit integer, so this is a hack to sign-extend 16 bits
        temp = temp / 256.0 #scale thermometer number to celcius
        return temp

    def __exit__(self):
        """If necessary, deallocate resources"""
        pass

