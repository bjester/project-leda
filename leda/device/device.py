import abc

class Device(object, metaclass = abc.ABCMeta):
    interval = 0

    @abc.abstractmethod
    def start(self, interval):
        pass

    @abc.abstractmethod
    def capture(self):
        pass

    @abc.abstractmethod
    def end(self):
        pass
