"""" Using the DS1631 Digital Thermostat"""""
"Converts Temperature-to-digital Word in 750ms (max)"

from leda.device import device

class Thermo(device.Device):
    """Project Ledas Thermostat object"""

    # __init__(self, extraParams) acts like a constructor but this is a normal function
    def init(self, time):
        """Init resources and attach interval for recurring capture"""
        pass
    
    def capture(self):
        """Capture temperature data"""
        pass

    def end(self):
        """If necessary, deallocate resources"""
        pass
