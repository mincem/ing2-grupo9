from Meter import *
from PostProvider import *
from PostQualifier import *

class RatingMeter(Meter):
    """Class to measure the rating"""
    def __init__(self, tvShow, aDate):
        self._tvShow = tvShow
        self._date = aDate
        super(RatingMeter, self).__init__()

    def getTvShow(self):
        return self._tvShow

    def getDate(self):
        return self._date

    def measure(self):
        aPostProvider = PostProvider()
        """aPostQualifier = PostQualifier()"""

        """posts = aPostProvider.postsFromDate(self._tvShow, self._date)
        qposts = aPostQualifier.qualify(posts)"""
        
        qposts = aPostProvider.postsFromDateWithSentiment(self._tvShow, self._date)
        self.notify(qposts)
