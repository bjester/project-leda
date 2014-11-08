from leda.device.position import GPS

class MockSession():

    def next(self):
        report = {'class': 'TPV'}
        return report


class MockGPS(GPS):

    def begin(self):
        self.session = MockSession()
