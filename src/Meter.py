from abc import *
from Observable import *

class Meter(Observable):
    """Abstract Class for different types of meters."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        super(Meter, self).__init__()
        pass

    @abstractmethod
    def measure(self, tvShow):
        pass
