from Observer import *
from Rating import *
from Sentiment import *

class MeasureView(Observer): 
    def __init__(self):
        self._rating = Rating(0)
        
    def update(self, qualifiedPosts):
        count = 0 
        for qpost in qualifiedPosts:
            if isinstance (qpost.getSentiment(),
                           PositiveSentiment):
                count = count + 1
        
        self._rating = Rating(count)
    

    def getRating(self):
        return self._rating
        
