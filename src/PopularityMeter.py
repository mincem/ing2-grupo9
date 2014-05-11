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
    
    def measure(self, aPostProvider, aPostQualifier):
        posts = aPostProvider.posts(self._tvShow, 
                                    self._initialDate,
                                    self._finalDate)
        
        for post in posts:
            qualifyPost = aPostQualifier.qualify(post)
            qualifyPosts.add(qulifyPost)
        self.notify(posts)
