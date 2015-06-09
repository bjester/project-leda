import gps
from leda.device import device

class PiGps(device.Device):
    """Project Leda GPS object"""
    session = None
    altitude = -1

    def __init__(self, device, baud, timout=1):
        self.logger = logger

    def __enter__(self, time):
        """Init resources"""
        self.session = gps.gps("localhost", "2947")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    
    def capture(self):
        """Store GPS data"""
        self.altitude = None
        self.report = self.__retrieve()
        self.logger.record([self.report.latitude])

    def __exit__(self):
        """If necessary, deallocate resources"""
        self.session = None


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


    def get_position(self):
        """To return position, (latitude, longitude)"""
        pass


    def get_altitude(self):
        """Get altitude as of last capture"""
        return self.altitude

