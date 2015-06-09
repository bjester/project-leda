#import theGPSlibrary
import gps
from leda.device import device

class GPS(device.Device):
    """Project Leda GPS object"""
    session = None
    report = None
    logger = None

    def __init__(self, logger):
        self.logger = logger

    # __init__(self, extraParams) acts like a constructor but this is a normal function
    def begin(self, time):
        """Init resources and attach interval for recurring capture"""
        self.session = gps.gps("localhost", "2947")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    
    def capture(self):
        """Store GPS data"""
        self.report = self.__retrieve()
        self.logger.record([self.report.latitude])

    def __retrieve(self):
        """Make call to GPS session to retrieve data"""
        if self.session is None:
            raise RuntimeError('GPS needs session to be set')

        try:
            report = self.session.next()

            if report['class'] == 'TPV':
                return report

        except StopIteration:
            self.end()

     # How do we want to do the following
     #def transmit():
     #    """Transmit GPS data to Tracking Radio"""

    def end(self):
        """If necessary, deallocate resources"""
        self.session = None

    def get_position(self):
        """To return position, (latitude, longitude)"""
        pass

    def get_altitude(self):
        """To return altitude"""
        pass
