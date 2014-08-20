import abc

class Device(object, metaclass=abc.ABCMeta):
    time = 0

    @abc.abstractmethod
    def init(self, time):
        """Init resources and attach interval for recurring capture"""
        pass

    @abc.abstractmethod
    def capture(self):
        pass

    @abc.abstractmethod
    def end(self):
        pass
