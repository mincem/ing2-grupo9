from PostFiltererDecorator import PostFiltererDecorator
from Post import Post
from Twitter import *
from TVShow import TVShow

class ByHourPostFilterer(PostFiltererDecorator):

    def __init__(self, aPostFilterer, startDateTime, endDateTime):
        self._aPostFilterer = aPostFilterer
        self._startDateTime = startDateTime
        self._endDateTime = endDateTime

    def getPosts(self):
        # TODO
        originalPosts = aPostFilterer.getPosts()
        posts = []
        for post in originalPosts:
            if (post.getDateTime() >= self._startDateTime and post.getDateTime() <= self._endDateTime):
                posts.append(post)
        return posts
