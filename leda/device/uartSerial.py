"""" Daughter Board - Pi serial interface"""""
import device
import serial

class UartSerial(device.Device):
    """Project Ledas Serial object"""


    def __init__(self, device_path, baud, tout):
        """Init resources and attach interval for recurring commands"""
        self.device = device_path
        self.port = serial.Serial(device_path, baud, tout)


    def capture(self):
        """Capture all daughter board sensor data"""
        # request 'S\r\n'
        self.port.write('S\r\n')
        # wait for Ack that data is ready  (receive 'A\r\n')
        ack = serialobj.read(3);
        if ack == 'A\r\n' :
            return false # received bad data

        # request the data
        self.port.write('R\r\n')
        # while last two bits are not \r\n
        bytes = []
        while bytes[-(bytes.size-1):-bytes.size] != '\r\n' :
            bytes += serialobj.read(1)

        return bytes[:bytes.size-2]


    def end(self):
        """If necessary, deallocate resources"""
        self.port.close()

