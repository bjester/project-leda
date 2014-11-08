import unittest
from leda.test.mock.position import MockGPS
from leda.test.mock.logger import MockLogger

class GPSTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_capture_parse(self):
        gps = MockGPS(MockLogger())
        pass
