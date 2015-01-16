"""" Using the ??? Radio"""""
"Transmit data to ground station (position & ?anything else)"
"""Using the ???? (URL TO DATASHEET)"""
from leda.device import device

class Radio(device.Device):
    """Project Ledas Radio object"""

    def __init__(self):
        pass


    def __enter__(self):
        """Init resources"""
        pass    

    def __exit__(self):
        """If necessary, deallocate resources"""
        pass

    # We probably arent receiving anything
    def capture(self):
        """Capture ??? data"""
        pass

    
    def transmit(self, position):
        """Transmit position"""
        pass
