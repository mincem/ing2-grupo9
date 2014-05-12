import Post

class QualifiedPost:
    
    def __init__(self, aPost, sentiment = ""):
        self._sentiment = sentiment
        self._post = aPost

    def getTime(self):
        return self._post.getTime()

    def getContent(self):
        return self._post.getContent()
    
    def getTvShow(self):
        return self._post.getTVShow()

    def getSentiment(self):
        return self._sentiment
