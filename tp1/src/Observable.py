from abc import *

class Observable: 
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def __init__(self):
        self._observers = []

    def getObservers(self):
        return self._observers
    
    @abstractmethod
    def notify(self, data):
        for observer in self._observers:
            observer.update(data)
        
    
    @abstractmethod
    def subscribe(self, anObserver):
        self._observers.append(anObserver)
            
    @abstractmethod
    def unsubscribe(self, anObserver):
        self._observers.remove(anObserver)
