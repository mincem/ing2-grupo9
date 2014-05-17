
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
    
    def isPositive():
        return true

    def isNegative():
        return false

class NegativeSentiment(Sentiment):
    def __str__(self):
        return "Negativo"

    def isPositive():
        return false

    def isNegative():
        return true

class NeutralSentiment(Sentiment):
    def __str__(self):
        return "Neutro"

    def isPositive():
        return false

    def isNegative():
        return false
