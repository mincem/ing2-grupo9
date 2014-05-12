from BasicPostFilterer import BasicPostFilterer
from Post import Post
from TwitterConector import TwitterConector
from TVShow import TVShow

class TweetToPostFilterer(BasicPostFilterer):

    def __init__(self, initialDate, finalDate, tvShow):
        self._initialDate = initialDate
        self._finalDate = finalDate
        self._tvShow = tvShow

    def Posts(self):
        t = TwitterConector()
        return t.tweetsBasicRequest(_initialDate, _finalDate, tvShow.getHashtags)
    
