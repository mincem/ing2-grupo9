from BasicPostFilterer import BasicPostFilterer
from Post import Post
from TwitterAdapter import *
from TVShow import TVShow

class TweetToPostFilterer(BasicPostFilterer):

    def __init__(self, initialDate, finalDate, tvShow):
        self._initialDate = initialDate
        self._finalDate = finalDate
        self._tvShow = tvShow

    def getPosts(self):
        twitterAdapter = TwitterAdapter()
        posts = []
        tweets = twitterAdapter.fetchTweets(self._initialDate,
                                            self._finalDate,
                                            self._tvShow.getKeywords())
        # Los tweets van a venir del adapter en Json y con eso tengo que crear los post
        for tweet in tweets['statuses']:
            posts.append(self.JsonToPost(tweet))
        return posts

    def getTVShow(self):
        return self._tvShow

    
    def JsonToPost(self, tweetJson):
            # Revisar esta fucnión cuando esté el adapter
            author = tweetJson['user']['screen_name']
            dateTime = tweetJson['created_at']
            content = tweetJson['text']
            tvShow = self._tvShow
            return Post(content, dateTime, author, tvShow)
