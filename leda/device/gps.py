from .gps3 import gps3

CONVERSION = {'raw': (1, 1, 'm/s', 'meters'),
              'metric': (3.6, 1, 'kph', 'meters'),
              'nautical': (1.9438445, 1, 'kts', 'meters'),
              'imperial': (2.2369363, 3.2808399, 'mph', 'feet')}


def unit_conversion(thing, units, length=False):
    """converts base data between metric, imperial, or natical units"""
    if 'n/a' == thing:
        return 'n/a'
    try:
        thing = round(thing * CONVERSION[units][0 + length], 2)
    except:
        thing = 'fubar'
    return thing, CONVERSION[units][2 + length]


class GPS:
    def __init__(self, host, port, debug_obj):
        self.gps_connection = gps3.GPSDSocket(host=host, port=port)
        self.gps_fix = gps3.Fix()
        self.debug = debug_obj
        self.units = 'metric'

    def wait(self):
        for new_data in self.gps_connection:
            if new_data:
                self.gps_fix.refresh(new_data)
                if self.gps_fix.TPV['alt'] != 'n/a':
                    break
                else:
                    self.debug.write('GPS: waiting for fix')

    def capture(self):
        new_data = self.gps_connection.next()

        if new_data:
            self.gps_fix.refresh(new_data)

        return [
            str(self.gps_fix.TPV['time']),
            str(self.gps_fix.TPV['lat']),
            str(self.gps_fix.TPV['lon']),
            str(unit_conversion(self.gps_fix.TPV['alt'], self.units, length=True)[0]),
            str(unit_conversion(self.gps_fix.TPV['speed'], self.units)[0]),
            str(self.gps_fix.TPV['track']),
            str(unit_conversion(self.gps_fix.TPV['climb'], self.units, length=True)[0]),
            str(self.gps_fix.TPV['mode']),
            str(unit_conversion(self.gps_fix.TPV['epx'], self.units, length=True)[0]),  # lat error
            str(unit_conversion(self.gps_fix.TPV['epy'], self.units, length=True)[0]),  # lon error
            str(unit_conversion(self.gps_fix.TPV['epv'], self.units, length=True)[0]),  # alt error
            str(unit_conversion(self.gps_fix.TPV['eps'], self.units, length=True)[0])  # speed error
        ]

