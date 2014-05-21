class Post:
    
    def __init__(self, content, aDateTime, author, tvShow):
        self._dateTime = aDateTime
        self._content = content
        self._author = author
        self._tvShow = tvShow

    def getDateTime(self):
        return self._dateTime

    def getContent(self):
        return self._content

    def getAuthor(self):
        return self._author
    
    def getTVShow(self):
        return self._tvShow
