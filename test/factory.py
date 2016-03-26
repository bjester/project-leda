class Camera:
    """Project Ledas camera object"""

    def __init__(self, path):
        print("Camera: initialized with path '{!s}'".format(path))

    def capture(self, timeStamp):
        print("Camera: capture with timestamp {!s}".format(timeStamp))


class Uart:

    def __init__(self, device_path, baud, tout):
        print("Uart: initialize with path '{!s}', baud {}, timeout {}".format(device_path, baud, tout))
        self.output_data = False

    def reset(self):
        print("Uart: reset")

    def capture(self):
        print("Uart: capture")
        return self.output_data

    def close(self):
        print("Uart: closed")


class Logger:
    """Data logger, writes as CSV"""

    def __init__(self, path):
        print("Logger: initialized with path '{!s}'".format(path))

    def open(self):
        print("Logger: opened")

    def append(self, data, timeStamp):
        print("Logger: capture with data '{!s}', timestamp {!s}".format(data, timeStamp))

    def close(self):
        print("Logger: closed")


class Factory:
    """Builds objects for Leda"""

    def build_camera(self, image_path):
        return Camera(image_path)

    def build_uart(self, serial_path, baudrate, serial_timeout):
        return Uart(serial_path, baudrate, serial_timeout)

    def build_logger(self, log_path):
        return Logger(log_path)
