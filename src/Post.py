class Post:
    
    def __init__(self, content, time, tvShow = ""):
        self._time = time
        self._content = content
        self._tvShow = tvShow

    def getTime(self):
        return(self._time)

    def getContent(self):
        return(self._content)
    
    def getTvShow(self):
        return self._tvShow
    
