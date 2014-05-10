class Post:
    
    def __init__(self, content, time, sentiment = "", tvShow = ""):
        self._time = time
        self._content = content
        self._sentiment = sentiment
        self._tvShow = tvShow

    def getTime(self):
        return(self.time)

    def getContent(self):
        return(self.content)

    
