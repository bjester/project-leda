"""" Daughter Board - Pi serial interface"""""
import device

class uartSerial(device.Device):
    """Project Ledas Serial object"""


    # __init__(self, extraParams) acts like a constructor but this is a normal function
    #bus should be a SMBus initialized externally. I'd like to only have one instance of I2C shared by all the devices
    #address should be the thermometer's address on I2C
    def __init__(self, device_path, baud, tout):
        """Init resources and attach interval for recurring commands"""
        self.RECV_BYTES = 1 #one byte at a time
        self.device = device_path
        self.port = serial.Serial(device_path, baudrate=baud, timeout=tout)


    def capture(self):
        """Capture all daughter board sensor data"""
        # request 'S\r\n'
        self.port.write('S')
        self.port.write('\r')
        self.port.write('\n')

        # wait for Ack that data is ready  (receive 'A\r\n')
        # while last two bits are not \r\n
        block = self.port.read(self.RECV_BYTES) #get temp

        return (temp, humidity, pressure, accel_x, accel_y, accel_z)


    def end(self):
        """If necessary, deallocate resources"""
        self.port.close()
        pass
