from Meter import *

class RatingMeter(Meter):
    """Class to measure the rating"""
    def __init__(self, tvShow):
        self._tvShow = tvShow
        super(RatingMeter, self).__init__()

    def getTvShow(self):
        return self._tvShow

    def notify(posts):
        super.notify(post)
    
    def measure(self, aPostProvider, aPostQualifier):
        posts = aPostProvider.posts(tvShow)
        for post in posts:
            qualifyPost = aPostQualifier.qualify(post)
            qualifyPosts.add(qulifyPost)
        self.notify(posts)

    def subscribe(anObserver):
        super.subscribe(anObserver)
            
    def unsubscribe(anObserver):
        super.unsubscribe(anObserver)
