class QualifiedWord:
    """A word with a value that represents its 'positiveness'."""
    def __init__(self, word):
        self._word = word
    
    def value(self):
        raise Exception("QualifiedWord.value: abstract method")
    
    def word(self):
        return self._word

class PositiveWord(QualifiedWord):
    def __init__(self, word):
        QualifiedWord.__init__(self, word)
    
    def value(self):
        return +1

class NegativeWord(QualifiedWord):
    def __init__(self, word):
        QualifiedWord.__init__(self, word)
    
    def value(self):
        return -1
