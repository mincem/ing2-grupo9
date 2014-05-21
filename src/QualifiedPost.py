import Post

class QualifiedPost:
    
    def __init__(self, aPost, sentiment = ""):
        self._sentiment = sentiment
        self._post = aPost

    def getDateTime(self):
        return self._post.getDateTime()

    def getContent(self):
        return self._post.getContent()
    
    def getTVShow(self):
        return self._post.getTVShow()

    def getSentiment(self):
        return self._sentiment

    def getAuthor(self):
        return self._post.getAuthor()
