from Meter import *
from Post import Post
from PostWithSentiment import *
from PostFilterer import PostFilterer
from BasicPostFilterer import BasicPostFilterer
from TweetToPostFilterer import TweetToPostFilterer
from SentimentClassifier import *

import datetime

class PostProvider:

    def __init__(self):
        pass

    def postsFromPeriod(self, tvShow, initialDate, finalDate):
        filterer = TweetToPostFilterer(initialDate, finalDate, tvShow)
        return filterer.Posts()


    def postsFromDate(self, tvShow, aDate):
        """ Para filtrar los de un solo día se llama con ese mismo día
            como comienzo y como final """
        filterer = TweetToPostFilterer(aDate, aDate, tvShow)
        return filterer.Posts()

    def postsWithSentimentFromPeriod(self, tvShow, initialDate, finalDate):
        posts = self.postsFromPeriod(tvShow, initialDate, finalDate)
        mySentimentClassifier = FileSentimentClassifier("positive_words.txt", "negative_words.txt")
        postsWithSentiment = []
        for p in posts:
            sentiment = sc.classify(p.getContent)
            postsWithSentiment.append(PostWithSentiment(p, sentiment))
        return postsWithSentiment

    def postsWithSentimentFromDate(self, tvShow, aDate):
        posts = self.postsFromDate(tvShow, aDate)
        mySentimentClassifier = FileSentimentClassifier("positive_words.txt", "negative_words.txt")
        postsWithSentiment = []
        for p in posts:
            sentiment = mySentimentClassifier.classify(p.getContent())
            postsWithSentiment.append(PostWithSentiment(p, sentiment))
        return postsWithSentiment
