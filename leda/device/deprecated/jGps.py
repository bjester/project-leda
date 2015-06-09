import serial
from leda.device import device

class PiGps(device.Device):
    """Project Leda GPS object"""

    def __init__(self, device, baud, tout=1):
        self.altitude = -1
        self.ser = serial.Serial(device, baud, tout)

    # WHEN using "with", this ensures that __exit__() is called on object destruction
    def __enter__(self):
        """Init resources"""
        pass

    def capture(self):
        """Store GPS data"""
        self.altitude = self.ser.read()
        return self.altitude
        
    def __exit__(self):
        """If necessary, deallocate resources"""
        pass



    def get_position(self):
        """To return position, (latitude, longitude)"""
        pass

    def get_altitude(self):
        """Get altitude as of last capture"""
        return self.altitude

