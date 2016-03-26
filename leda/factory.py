from .device import camera, uart
from .data import logger


class Factory:
    """Builds objects for Leda"""

    def __init__(self, debug_obj):
        self.debug = debug_obj

    def build_camera(self, image_path):
        return camera.Camera(image_path, self.debug)

    def build_uart(self, serial_path, baud_rate, serial_timeout):
        return uart.Uart(serial_path, baud_rate, serial_timeout, self.debug)

    def build_logger(self, log_path):
        return logger.Logger(log_path, self.debug)
