from PostFilterer import PostFilterer
from abc import *

class PostFiltererDecorator(PostFilterer):
    __metaclass__=ABCMeta

    @abstractmethod
    def Posts(self):
        pass
    

