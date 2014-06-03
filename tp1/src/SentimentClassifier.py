from Sentiment import NegativeSentiment
from Sentiment import PositiveSentiment
from Sentiment import NeutralSentiment

from QualifiedWord import PositiveWord
from QualifiedWord import NegativeWord

class SentimentClassifier:
    """Abstract class for sentiment classifiers."""
    
    def classify(self, text):
        """Classify a text as 'positive', 'negative' or 'neutral'."""
        raise Exception("SentimentClassifier.classify: abstract method")

class WordListSentimentClassifier(SentimentClassifier):
    """Sentiment classifier based on  a list of QualifiedWord's."""
    
    def __init__(self, qualified_words):
        self._qualified_words = qualified_words
    
    def classify(self, text):
        words = text.split()
        
        value = 0
        for word in words:
            #changes to lowercase and strips leading and trailing punctuation marks
            word = word.lower().strip(";.,")
            
            for qword in self._qualified_words:
                if word == qword.word():
                    value += qword.value()
        
        return self.getSentiment(value)
    
    def getSentiment(self, positiveness_value):
        """Returns a new Sentiment according to a positiveness value"""
        if positiveness_value < 0:
            return NegativeSentiment()
        elif positiveness_value > 0:
            return PositiveSentiment()
        else:
            return NeutralSentiment()

class FileSentimentClassifier(WordListSentimentClassifier):
    """WordListSentimentClassifier that obtains the qualified words from two text files."""
    
    def __init__(self, positive_filename, negative_filename):
        positive_words = self.getWordsFromFile(positive_filename)
        negative_words = self.getWordsFromFile(negative_filename)
        
        qualified_words = []
        qualified_words.extend(map(PositiveWord, positive_words))
        qualified_words.extend(map(NegativeWord, negative_words))
        
        WordListSentimentClassifier.__init__(self, qualified_words)
        
    def getWordsFromFile(self, filename):
        words = []
        
        with open(filename) as file:
            for line in file:
                word = line.strip().lower()
                if word:
                    words.append(word)
        
        return words
