from SentimentClassifier import FileSentimentClassifier

from Sentiment import PositiveSentiment
from Sentiment import NegativeSentiment
from Sentiment import NeutralSentiment


if __name__ == "__main__":
    sc = FileSentimentClassifier("positive_words.txt", "negative_words.txt")
    
    phrases = [
        ("Ese munieco es algo malo",                    NegativeSentiment),
        ("El bien y el mal definen por penal",          NeutralSentiment),
        ("Lo bueno, si breve, dos veces bueno",         PositiveSentiment),
        ("Pense que era bueno pero era malo, malisimo", NegativeSentiment)
    ]
    
    for (phrase, expected_sentiment_type) in phrases:
        sentiment = sc.classify(phrase)
        print str(sentiment) + ": " + phrase
        if not isinstance(sentiment, expected_sentiment_type):
            raise Exception("Expected {0} but got {1} classifying phrase '{2}'".format(expected_sentiment_type, sentiment.__class__, phrase))
    
else:
    raise Exception("Cannot use as module")