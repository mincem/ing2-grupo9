from abc import *

class PostFilterer(metaclass=ABCMeta):

    @abstractmethod
    def getPosts(self):
        pass

