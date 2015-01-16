from leda.device.position import GPS
#  NOTE THAT:  this file should be nearly identical to the mock piGps.py file

class MockSession():

    def next(self):
        report = {'class': 'TPV'}
        return report


class MockGPS(GPS):

    def begin(self):
        self.session = MockSession()
