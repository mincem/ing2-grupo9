class Post:
    
    def __init__(self, content, time, author, tvShow):
        self._time = time
        self._content = content
        self._author = author
        self._tvShow = tvShow

    def getTime(self):
        return self._time

    def getContent(self):
        return self._content

    def getAuthor(self):
        return self._author
    
    def getTVShow(self):
        return self._tvShow
    
