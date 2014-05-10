from PostFilterer import PostFilterer
from abc import *

class BasicPostFilterer(PostFilterer):
    __metaclass__=ABCMeta

    @abstractmethod
    def Posts(self):
        pass
    

