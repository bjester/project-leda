import abc

class Device(object, metaclass = abc.ABCMeta):
    time = 0

    @abc.abstractmethod
    def start(self, time):
        pass

    @abc.abstractmethod
    def capture(self):
        pass

    @abc.abstractmethod
    def end(self):
        pass
