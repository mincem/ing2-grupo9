from Post import *
from Sentiment import *

class PostWithSentiment:
    
    def __init__(self, post, sentiment):
        self._post = post
        self._sentiment = sentiment

    def getPost(self):
        return (self._post)

    def getSentiment(self):
        return (self._sentiment)
    
    
