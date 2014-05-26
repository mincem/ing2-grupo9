from Observer import *
from Measure import *

class MeasureView(Observer): 
    def __init__(self):
        self._measure = Measure(0)
        self._total = Measure(0)

    def update(self, qualifiedPosts):
        count = 0 
        for qpost in qualifiedPosts:
            if not qpost.getSentiment().isNegative():
                count = count + 1
        
        self._measure = Measure(count)
    
    def getMeasure(self):
        return self._measure

    def getTotalPosts(self):
        return self._total
    
