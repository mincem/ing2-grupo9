from Meter import *
from PostProvider import *

class RatingMeter(Meter):
    """Class to measure the rating"""
    def __init__(self, tvShow, aDate):
        self._date = aDate
        super(RatingMeter, self).__init__(tvShow)

    def getDate(self):
        return self._date

    def measure(self):
        if self._qPosts == []:
            aPostProvider = PostProvider()
            self._qPosts = aPostProvider.qualifiedPostsDuringAirtime(self._tvShow,
                                                                     self._date)
        self.notify(self._qPosts)
