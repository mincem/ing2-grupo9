from Observer import *

class PostsView(Observer): 
    def __init__(self):
        self._qPosts = []
        
    def update(self, qualifiedPosts):
        self._qPosts = qualifiedPosts

    def getPosts(self):
        return self._qPosts
