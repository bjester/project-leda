"""" Using the ??? Radio"""""
"Transmit data to ground station (position & ?anything else)"
"""Using the ???? (URL TO DATASHEET)"""
from leda.device import device

class Radio(device.Device):
    """Project Ledas Radio object"""
    def init(self)
        """Init resources and attach interval for recurring capture"""
        pass
    
    # We probably arent receiving anything
    def capture(self):
        """Capture ??? data"""
        pass

    def end(self):
        """If necessary, deallocate resources"""
        pass
    
    def transmit(self, position):
        """Transmit position"""
        pass
