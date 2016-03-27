"""" Daughter Board - Pi serial interface"""""
import serial
import time
import io


class Uart:
    RECEIVED_BYTES = 26
    SIZE_CMD = 2  # readline doesn't use this
    CMD_ACK = 'Z\n'
    CMD_REQUEST = 'S\n'
    CMD_READ = 'R\n'
    CMD_RESET = 'W\n'

    def __init__(self, device_path, baud, tout, debug_obj):
        """Init resources and attach interval for recurring commands"""
        self.device = device_path
        tout_seconds = tout
        self.ser = serial.Serial(device_path, baudrate=baud, timeout=tout_seconds)
        time.sleep(1)  # must give serial time to start
        self.ser.readline()  # serial sends "LEDA\n" upon establishing connection
        self.ser.flushInput()
        self.debug = debug_obj

    def reset(self):
        """If receiving bad data, reset daughter board"""
        self.ser.flushInput()
        self.ser.write(bytearray(self.CMD_RESET, 'ascii'))
        time.sleep(1)  # must give serial time to start
        self.ser.readline()  # serial sends "LEDA\n" upon establishing connection
        self.ser.flushInput()

    # EXPECT >750ms to pass between sending request and receiving ack
    # 1. timeout -> set up by python automatically
    # 2. \n can be encountered in middle of packet (unlikely) but byte for byte probably safer
    def capture(self):
        """Capture all daughter board sensor data"""

        # send request to begin ADC conversion
        self.ser.write(bytearray(self.CMD_REQUEST, 'ascii'))
        # wait for Ack indicating data ready to send
        ack = self.ser.readline().decode('ascii')

        if ack != self.CMD_ACK:
            self.reset()
            return False # received bad data

        # request the data
        self.ser.write(bytearray(self.CMD_READ, 'ascii'))

        # read the data; 14 bytes
        data = self.ser.readline()
        checksum = 0
        data_body = data[0:-2]  # 2nd to last byte is XOR checksum

        for x in data_body:
            checksum ^= int(x)

        if checksum == int(data[-2]):
            self.reset()
            return False  # received bad data
        return data.decode('ascii')

    def close(self):
        """If necessary, deallocate resources"""
        self.ser.close()

