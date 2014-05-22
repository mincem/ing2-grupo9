from PostFiltererDecorator import PostFiltererDecorator
from Post import Post
from Twitter import *
from TVShow import TVShow

class ByTimePostFilterer(PostFiltererDecorator):

    def __init__(self, aPostFilterer, startTime, endTime):
        self._aPostFilterer = aPostFilterer
        self._startTime = startTime
        self._endTime = endTime

    def getPosts(self):
        # TODO
        originalPosts = aPostFilterer.getPosts()
        posts = []
        for post in originalPosts:
            if (post.getDateTime().time() >= self._startTime and post.getDateTime().time() <= self._endTime):
                posts.append(post)
        return posts
