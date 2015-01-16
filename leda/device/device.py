### The interface common to all project Leda devices
### author:  Blaine Jester

class Device(object):
    """Enforces a common interface for all project Leda devices"""

    #abstractmethod
    # WHEN using "with", this ensures that __exit__() is called on object destruction
    def __enter__(self):
        """Init resources"""
        raise NotImplementedError('Abstract method not implemented')

    #abstractmethod
    def capture(self):
        """Take a picture, capture measurements, etc"""
        raise NotImplementedError('Abstract method not implemented')

    #abstractmethod
    def __exit__(self, type, value, traceback):
        """If necessary, deallocate resources"""
        raise NotImplementedError('Abstract method not implemented')

