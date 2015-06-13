"""" Daughter Board - Pi serial interface"""""
import serial
import time
import io

class Uart:
    RECEIVED_BYTES = 26
    CMD_BYTES = 2

    def __init__(self, device_path, baud, tout):
        """Init resources and attach interval for recurring commands"""
        self.device = device_path
        toutSeconds = tout/1000
        self.ser = serial.Serial(device_path, baudrate=baud, timeout=toutSeconds)
        time.sleep(1) #must give serial time to start
        self.ser.readline() #serial sends "LEDA\n" upon establishing connection
        self.ser.flushInput()


    def reset(self):
        """If receiving bad data, reset daughter board"""
        self.ser.flushInput()
        self.ser.write("W\n");
        time.sleep(1) #must give serial time to start
        self.ser.readline() #serial sends "LEDA\n" upon establishing connection
        self.ser.flushInput()

    # EXPECT >750ms to pass between sending request and receiving ack
    #1. timeout -> set up by python automatically
    #2. \n can be encountered in middle of packet (unlikely) but byte for byte probably safer
    def capture(self):
        """Capture all daughter board sensor data"""
        # request 'S\n'
        self.ser.write("S\n")
        # wait for Ack that data is ready  (receive 'A\n')
        ack = ""
        for x in range(0, self.CMD_BYTES):
            ack += self.ser.read();
        ack = "".join(ack)
        if ack != "Z\n":
            return False # received bad data
        print("Ack received")
        #print str(what)
        # request the data
        self.ser.write("R\n")
        # read the data; 14 bytes
        result = []
        for x in range(0, self.RECEIVED_BYTES):
            result += self.ser.read() 
        return "".join(result)

    def close(self):
        """If necessary, deallocate resources"""
        self.ser.close()


#TEST AREA
#uart = Uart("/dev/leda-db", 38400, 1000)
#cap = uart.capture()
#print("Received bad data" if cap == False else cap)
#cap = uart.capture()
#print("Received bad data" if cap == False else cap)
#cap = uart.capture()
#print("Received bad data" if cap == False else cap)
#uart.close()

