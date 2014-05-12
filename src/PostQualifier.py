from Meter import *
from Post import Post
from QualifyPost import QualifyPost
from PostFilterer import PostFilterer
from BasicPostFilterer import BasicPostFilterer
from TweetToPostFilterer import TweetToPostFilterer
from gui import HardcodedPost
from gui import HardcodedBadPost


from SentimentClassifier import FileSentimentClassifier
from Sentiment import PositiveSentiment
from Sentiment import NegativeSentiment
from Sentiment import NeutralSentiment


class PostQualifier:

    def qualify(self, posts):
        'TODO: do not hardcode this'
        qposts = []
        sc = FileSentimentClassifier("positive_words.txt",
                                     "negative_words.txt")
        
        for hpost in posts:
            post = Post(hpost.content(), hpost.date(),
                        hpost.author())
            sentiment = sc.classify(post.getContent())
            qposts.append(QualifyPost(post, sentiment))
        
        return qposts

   
