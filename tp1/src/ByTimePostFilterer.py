from PostFiltererDecorator import PostFiltererDecorator
from Post import Post
from TwitterAdapter import *
from TVShow import TVShow
import time
import datetime

class ByTimePostFilterer(PostFiltererDecorator):

    def __init__(self, aPostFilterer, startTime, endTime):
        self._aPostFilterer = aPostFilterer
        self._startTime = startTime
        self._endTime = endTime

    def getPosts(self):
        # TODO
        originalPosts = self._aPostFilterer.getPosts()
        posts = []
        for post in originalPosts:
            hour = post.getDateTime().tm_hour
            minutes = post.getDateTime().tm_min
            time = datetime.time(hour, minutes)
            if (time >= self._startTime and time <= self._endTime):
                posts.append(post)
        return posts
