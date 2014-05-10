from PostFiltererDecorator import PostFiltererDecorator
from TweeterConector import TweeterConector

class ByDatePostFiltererDecorator(PostFiltererDecorator):

    def __init__(self, aPostFilterer, initialDate, finalDate):
        self._aPostFilterer = aPostFilterer
        self._initialDate = initialDate
        self._finalDate = finalDate

    def Post(self):
        t = TweeterConector()
        return t.tweetsInPeriod(_initialDate, _finalDate)        
        
