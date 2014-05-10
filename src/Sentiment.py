
class Sentiment:
    """A sentiment extracted from a text."""
    pass

class PositiveSentiment(Sentiment):
    def __str__(self):
        return "sentimiento positivo"

class NegativeSentiment(Sentiment):
    def __str__(self):
        return "sentimiento negativo"

class NeutralSentiment(Sentiment):
    def __str__(self):
        return "sentimiento neutro"

