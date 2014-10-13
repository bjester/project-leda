#import theGPSlibrary
from leda.device import device

class GPS(device.Device):
    """Project Leda GPS object"""
    pass

    # __init__(self, extraParams) acts like a constructor but this is a normal function
    def init(self, time):
        """Init resources and attach interval for recurring capture"""
        pass
    
    def capture(self):
        """Store GPS data"""
        pass

     # How do we want to do the following
     #def transmit():
     #    """Transmit GPS data to Tracking Radio"""

    def end(self):
        """If necessary, deallocate resources"""
        pass
