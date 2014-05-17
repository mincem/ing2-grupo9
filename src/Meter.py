from abc import *
from Observable import *

class Meter(Observable):
    """Abstract Class for different types of meters."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, tvShow):
        super(Meter, self).__init__()
        self._tvShow = tvShow

    @abstractmethod
    def measure(self):
        pass

    def getTvShow(self):
        return self._tvShow
 
