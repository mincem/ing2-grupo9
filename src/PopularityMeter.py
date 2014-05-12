from Meter import *

class PopularityMeter(Meter):
    """Class to calculate the popularity"""
    def __init__(self, tvShow, initialDate, finalDate):
        self._tvShow = tvShow
        self._initialDate = initialDate
        self._finalDate = finalDate
        super(PopularityMeter, self).__init__()

    def getTvShow(self):
        return self._tvShow
        
    def getInitialDate(self):
        return self._initialDate

    def getFinalDate(self):
        return self._finalDate
    
    def measure(self):
        aPostProvider = PostProvider()
        aPostQualifier = PostQualifier()

        posts = aPostProvider.postsFromPeriod(self._tvShow, 
                                    self._initialDate,
                                    self._finalDate)
        
        qposts = aPostQualifier.qualify(posts)
        self.notify(qposts)
