from Meter import *
from Post import Post
from QualifyPost import QualifyPost

from gui import HardcodedPost
from gui import HardcodedBadPost

from SentimentClassifier import FileSentimentClassifier
from Sentiment import *

class PostQualifier:

    def qualify(self, posts):
        qposts = []
        sc = FileSentimentClassifier("positive_words.txt",
                                     "negative_words.txt")
        
        for post in posts:
            sentiment = sc.classify(post.getContent())
            qposts.append(QualifyPost(post, sentiment))
        
        return qposts
