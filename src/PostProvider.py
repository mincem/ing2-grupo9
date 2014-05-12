from Meter import *
from Post import Post
from PostFilterer import PostFilterer
from BasicPostFilterer import BasicPostFilterer
from TweetToPostFilterer import TweetToPostFilterer
from gui import HardcodedPost
from gui import HardcodedBadPost

import datetime

class PostProvider:
 
    def postsFromDate(self, TVShow, aDate):
        'TODO: do not hardcode this'
        return [HardcodedPost(), HardcodedBadPost()]

    def postsFromPeriod(self, TvShow, initialDate, finalDate):
        'TODO: do not hardcode this'
        return [HardcodedPost(), HardcodedBadPost()]

    # def posts(self, TVShow, aDate):
    #     return TweetToPostFilterer().Posts()

    # def posts(self, TvShow, initialDate, finalDate):
    #     return ByDatePostFiltererDecorator(initialDate,
    #                                        finalDate).Posts()

