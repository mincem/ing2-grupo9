from Meter import *
from Post import Post
from QualifiedPost import QualifiedPost

from SentimentClassifier import FileSentimentClassifier
from Sentiment import *

class PostQualifier:

    def qualify(self, posts):
        qposts = []
        sc = FileSentimentClassifier("positive_words.txt",
                                     "negative_words.txt")
        
        for post in posts:
            sentiment = sc.classify(post.getContent())
            qposts.append(QualifiedPost(post, sentiment))
        
        return qposts
