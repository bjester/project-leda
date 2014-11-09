### The interface common to all project Leda devices
### author:  Blaine Jester

class Device(object):
    """Enforces a common interface for all project Leda devices"""
    status = 'ready' # or 'busy' or 'suspended'

    #abstractmethod
    def begin(self):
        """Init resources and attach interval for recurring capture"""
        raise NotImplementedError('Abstract method not implemented')

    #abstractmethod
    def capture(self):
        """Take a picture, capture measurements, etc"""
        raise NotImplementedError('Abstract method not implemented')

    #abstractmethod
    def end(self):
        """If necessary, deallocate resources"""
        raise NotImplementedError('Abstract method not implemented')
