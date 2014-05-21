from Meter import *
from PostProvider import *

class PopularityMeter(Meter):
    """Class to calculate the popularity"""
    def __init__(self, tvShow, initialDate, finalDate):
        self._initialDate = initialDate
        self._finalDate = finalDate
        super(PopularityMeter, self).__init__(tvShow)
        
    def getInitialDate(self):
        return self._initialDate

    def getFinalDate(self):
        return self._finalDate
    
    def measure(self):
        """ mirar como está hecho en RatingMeter y modificarlo """
        aPostProvider = PostProvider()

        qposts = aPostProvider.postsWithSentimentFromPeriod(self._tvShow, 
                                    self._initialDate,
                                    self._finalDate)
        
        self.notify(qposts)
