from BasicPostFilterer import BasicPostFilterer
from Post import Post
from Twitter import *
from TVShow import TVShow

class TweetToPostFilterer(BasicPostFilterer):

    def __init__(self, initialDate, finalDate, tvShow):
        self._initialDate = initialDate
        self._finalDate = finalDate
        self._tvShow = tvShow

    def Posts(self):
        t = HardcodedTwitter()
        posts = []
        for key in self._tvShow.getKeywords():
            tweets = t.searchSinceUntil(key,
                                        self._initialDate,
                                        self._finalDate)
            for tweet in tweets['statuses']:
                posts.append(self.JsonToPost(tweet))
        return posts
        
    def JsonToPost(self, tweetJson):
            author = tweetJson['user']['screen_name']
            time = tweetJson['created_at']
            content = tweetJson['text']
            TVShow = self._tvShow
            return Post(content, time, author, TVShow)
