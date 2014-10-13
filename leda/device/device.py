### The interface common to all project Leda devices
### author:  Blaine Jester
import abc


class Device(object, metaclass=abc.ABCMeta):
    """Enforces a common interface for all project Leda devices"""
    time = 0

    @abc.abstractmethod
    def init(self, time):
        """Init resources and attach interval for recurring capture"""
        pass

    @abc.abstractmethod
    def capture(self):
        """Take a picture, capture measurements, etc"""
        pass

    @abc.abstractmethod
    def end(self):
        """If necessary, deallocate resources"""
        pass
