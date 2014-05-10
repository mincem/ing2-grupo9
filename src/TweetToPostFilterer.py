from BasicPostFilterer import BasicPostFilterer
from Post import Post
from TweeterConector import TweeterConector

class TweetToPostFilterer(BasicPostFilterer):

    def __init__(self, initialDate):
        self._initialDate = initialDate

    def Posts(self):
        t = TweeterConector()
        return t.tweetsSince(_initialDate)
