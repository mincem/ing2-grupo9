from BasicPostFilterer import BasicPostFilterer
from Post import Post
from Twitter import Twitter*
from TVShow import TVShow

class TweetToPostFilterer(BasicPostFilterer):

    def __init__(self, initialDate, finalDate, tvShow):
        self._initialDate = initialDate
        self._finalDate = finalDate
        self._tvShow = tvShow

    def Posts(self):
        t = HarcodedTwitter()
        posts = []
        for hashtag in tvShow.getHashtags:
			tweet = t.searchSinceUntil(hashtag, self._initialDate, self._finalDate)
			print(tweet)
			posts.append(JsonToPost(tweet))
		return posts
        

def JsonToPost(tweetJson):
	""" TODO """	
	return tweetJson
    
