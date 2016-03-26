class Camera:
    """Project Ledas camera object"""

    def __init__(self, path, debug_obj):
        self.debug = debug_obj
        self.debug.write("Camera: initialized with path '{!s}'".format(path))

    def capture(self, timeStamp):
        self.debug.write("Camera: capture with timestamp {!s}".format(timeStamp))


class Uart:

    def __init__(self, device_path, baud, tout, debug_obj):
        self.debug = debug_obj
        self.debug.write("Uart: initialize with path '{!s}', baud {}, timeout {}".format(device_path, baud, tout))
        self.output_data = False

    def reset(self):
        self.debug.write("Uart: reset")

    def capture(self):
        self.debug.write("Uart: capture")
        return self.output_data

    def close(self):
        self.debug.write("Uart: closed")


class Logger:
    """Data logger, writes as CSV"""

    def __init__(self, path, debug_obj):
        self.debug = debug_obj
        self.debug.write("Logger: initialized with path '{!s}'".format(path))

    def open(self):
        self.debug.write("Logger: opened")

    def append(self, data, timeStamp):
        self.debug.write("Logger: capture with data '{!s}', timestamp {!s}".format(data, timeStamp))

    def close(self):
        self.debug.write("Logger: closed")


class Factory:
    """Builds objects for Leda"""

    def __init__(self, debug_obj):
        self.debug = debug_obj

    def build_camera(self, image_path):
        return Camera(image_path, self.debug)

    def build_uart(self, serial_path, baudrate, serial_timeout):
        return Uart(serial_path, baudrate, serial_timeout, self.debug)

    def build_logger(self, log_path):
        return Logger(log_path, self.debug)
