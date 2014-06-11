from Observer import *

class PostsView(Observer): 
    def __init__(self):
        self._qPosts = []
        self._bySentimentFilter = ['Positivo']

    def update(self, qualifiedPosts):
        self._qPosts = qualifiedPosts

    def getPosts(self):
        return [i for i in self._qPosts if str(i.getSentiment()) in self._bySentimentFilter]

    def setSentimentFilter(self, aFilter):
        self._bySentimentFilter = aFilter

    def getTotalPosts(self):
        return len(self._qposts)
