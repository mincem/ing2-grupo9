from abc import *

class Sentiment(metaclass=ABCMeta):
    """A sentiment extracted from a text."""

    @abstractmethod
    def isPositive():
        pass

    @abstractmethod
    def isNegative():
        pass

class PositiveSentiment(Sentiment):
    def __str__(self):
        return "Positivo"
    
    def isPositive(self):
        return True

    def isNegative(self):
        return False

class NegativeSentiment(Sentiment):
    def __str__(self):
        return "Negativo"

    def isPositive(self):
        return False

    def isNegative(self):
        return True

class NeutralSentiment(Sentiment):
    def __str__(self):
        return "Neutro"

    def isPositive(self):
        return False

    def isNegative(self):
        return False
