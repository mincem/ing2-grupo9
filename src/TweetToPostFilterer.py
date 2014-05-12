from BasicPostFilterer import BasicPostFilterer
from Post import Post
from TweeterConector import TweeterConector
from TVShow import TVShow

class TweetToPostFilterer(BasicPostFilterer):

    def __init__(self, aPostFilterer, initialDate, finalDate, tvShow):
        self._aPostFilterer = aPostFilterer
        self._initialDate = initialDate
        self._finalDate = finalDate
        self._tvShow = tvShow

    def Post(self):
        t = TweeterConector()
        return t.tweetsBasicRequest(_initialDate, _finalDate, tvShow.getHashtags)

    
