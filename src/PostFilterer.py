from abc import *

class PostFilterer(metaclass=ABCMeta):

    @abstractmethod
    def Posts(self):
        pass

