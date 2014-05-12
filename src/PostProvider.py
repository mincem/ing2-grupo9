from Meter import *
from Post import Post
from PostFilterer import PostFilterer
from BasicPostFilterer import BasicPostFilterer
from TweetToPostFilterer import TweetToPostFilterer
from gui import HardcodedPost
from gui import HardcodedBadPost
from SentimentClassifier import *

import datetime

class PostProvider:
 """
    def postsFromDate(self, TVShow, aDate):
        'TODO: do not hardcode this'
        return [HardcodedPost(), HardcodedBadPost()]

    def postsFromPeriod(self, TvShow, initialDate, finalDate):
        'TODO: do not hardcode this'
        return [HardcodedPost(), HardcodedBadPost()]
 """

    def postsFromPeriod(self, tvShow, initialDate, finalDate):
        filterer = TweetToPostFilterer(initialDate, finalDate, tvShow)
        return filterer.posts()


    def postsFromDate(self, tvShow, aDate):
        """ Para filtrar los de un solo día se llama con ese mismo día
            como comienzo y como final """
        filterer = TweetToPostFilterer(aDate, aDate, tvShow)
        return filterer.posts()

    def postsWithSentimentFromPeriod(self, tvShow, initialDate, finalDate):
        posts = postsFromPeriod(tvShow, initialDate, finalDate)
        mySentimentClassifier = FileSentimentClassifier("positive_words.txt", "negative_words.txt")
        postsWhitSentiment = []
        for p in posts:
			sentiment = sc.classify(p.getContent)
			postsWhithSentiment.append(PostWithSentiment(p, sentiment)
		return postsWithSentiment

    def postsWhithSentimentFromDate(self, tvShow, aDate):
        posts = postsFromDate(tvShow, aDate)
        mySentimentClassifier = FileSentimentClassifier("positive_words.txt", "negative_words.txt")
        postsWhitSentiment = []
        for p in posts:
			sentiment = sc.classify(p.getContent)
			postsWhithSentiment.append(PostWithSentiment(p, sentiment)
		return postsWithSentiment



    # def posts(self, TVShow, aDate):
    #     return TweetToPostFilterer().Posts()

    # def posts(self, TvShow, initialDate, finalDate):
    #     return ByDatePostFiltererDecorator(initialDate,
    #                                        finalDate).Posts()

