"""" Using the DS1631 Digital Thermostat"""""
"Converts Temperature-to-digital Word in 750ms (max)"

from leda.device import device
import smbus

class Thermo(device.Device):
    """Project Ledas Thermostat object"""
    bus = None
    address = None
    # __init__(self, extraParams) acts like a constructor but this is a normal function
    def init(self, time, address, bus):
        """Init resources and attach interval for recurring capture"""
        self.bus = bus
        self.address = address
    
    def capture(self):
        """Capture temperature data"""
        temp = self.bus.read_word_data(self.address,0xAA)
        temp = (temp/256+temp*256)%65536
        if temp & 0x8000:
            temp = temp - 0x10000
        temp = temp / 256.0
        return temp

    def end(self):
        """If necessary, deallocate resources"""
        pass
