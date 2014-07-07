from Post import *
from TweetToPostFilterer import *
from QualifiedPost import *
from SentimentClassifier import FileSentimentClassifier
from ByTimePostFilterer import *
import datetime

class PostProvider:

    def __init__(self, decision):
        self._decision = decision

    def postsFromPeriod(self, tvShow, initialDate, finalDate):
        filterer = TweetToPostFilterer(initialDate, finalDate, tvShow, self.decision)
        return filterer.getPosts()

    def postsFromDuringAirtime(self, tvShow, aDate):
        """ Para filtrar los de un solo día se llama con ese mismo día
            como comienzo y como final """
        untilDate = aDate + datetime.timedelta(days=1)
        basicFilterer = TweetToPostFilterer(aDate, untilDate, tvShow, self._decision)
        startTime = basicFilterer.getTVShow().getStartTime()
        endTime = basicFilterer.getTVShow().getEndTime()
        timeFilterer = ByTimePostFilterer(basicFilterer, startTime, endTime)
        return timeFilterer.getPosts()

    def qualifiedPostsFromPeriod(self, tvShow, initialDate, finalDate):
        posts = self.postsFromPeriod(tvShow, initialDate, finalDate)
        mySentimentClassifier = FileSentimentClassifier("positive_words.txt", "negative_words.txt")
        qualifiedPosts = []
        for p in posts:
            sentiment = mySentimentClassifier.classify(p.getContent())
            qualifiedPosts.append(QualifiedPost(p, sentiment))
        return qualifiedPosts

    def qualifiedPostsDuringAirtime(self, tvShow, aDate):
        """ esto me parece que hay que cambiarlo para que tome dos DateTime
        porque eso es lo que se necesita para el rating """
        posts = self.postsFromDuringAirtime(tvShow, aDate)
        mySentimentClassifier = FileSentimentClassifier("positive_words.txt", "negative_words.txt")
        qualifiedPosts = []
        for p in posts:
            sentiment = mySentimentClassifier.classify(p.getContent())
            qualifiedPosts.append(QualifiedPost(p, sentiment))
        return qualifiedPosts
