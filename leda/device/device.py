import abc

class Device(object, metaclass=abc.ABCMeta):
    interval = 0

    @abc.abstractmethod
    def init(self, interval):
        """Init resources and attach interval for recurring capture"""
        pass

    @abc.abstractmethod
    def capture(self):
        pass

    @abc.abstractmethod
    def end(self):
        pass
