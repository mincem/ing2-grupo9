from Meter import *

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

    def measure(self, aPostProvider, aPostQualifier):
        posts = aPostProvider.posts(tvShow)
        for post in posts:
            qualifyPost = aPostQualifier.qualify(post)
            qualifyPosts.add(qulifyPost)
        self.notify(posts)
