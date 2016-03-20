from .device import camera, uart
from .data import logger

class Factory:
    """Builds objects for Leda"""

    def build_camera(self, image_path):
        return camera.Camera(image_path)

    def build_uart(self, serial_path, baudrate, serial_timeout):
        return uart.Uart(serial_path, baudrate, serial_timeout)

    def build_logger(self, log_path):
        return logger.Logger(log_path)
