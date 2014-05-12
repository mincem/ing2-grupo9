from twython import Twython, TwythonError
from TVShow import *
import json

class Twitter:
    def __init__(self):
        self._APP_KEY = 'D0PYmI7UMWHyzISn4Z7hPx8Mc'
        self._APP_SECRET = 'NNPnwOereOGZhzDxYrRrgM7IvU8khzSW5zT4F2F8LKs5yBwJz1'
        
    def searchFrom(self, keyword, date):
        twitter = Twython(self._APP_KEY, self._APP_SECRET)
        auth = twitter.get_authentication_tokens()
        OAUTH_TOKEN = auth['oauth_token']
        OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
        
        twitterFinal = Twython(self._APP_KEY, self._APP_SECRET,
                               OAUTH_TOKEN,
                               OAUTH_TOKEN_SECRET)
        
        query = keyword + ' until:' + date
        
        try:
            search_results = twitter.search(q=query,
                                            count=100)
        except TwythonError as e:
            print(e)
            
        return search_results
        
    def searchSinceUntil(self, keyword, initialDate, finalDate):
        twitter = Twython(self._APP_KEY, self._APP_SECRET)
        auth = twitter.get_authentication_tokens()
        OAUTH_TOKEN = auth['oauth_token']
        OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
        
        twitterFinal = Twython(self._APP_KEY, self._APP_SECRET, 
                               OAUTH_TOKEN, 
                               OAUTH_TOKEN_SECRET)      

        query = keyword + ' since:' + iniitalDate + ' until:' + finalDate
        
        try:
            search_results = twitter.search(q=query, count=100)
        except TwythonError as e:
            print(e)
            
        return search_results

class HardcodedTwitter(Twitter):
    def __init__(self):
        super(HardcodedTwitter, self).__init__()
        
    def searchFrom(self, keyword, date):
        if any(keyword in s for s in
               BailandoTVShow().getHashtags()):
            filename = "bailandoTweets"
        else:
            filename = "678Tweets"

        with open(filename, "r") as f:
            return json.load(f)

    def searchSinceUntil(self, keyword, initialDate, finalDate):
        if any(keyword in s for s in
               BailandoTVShow().getHashtags()):
            filename = "BailandoTweets"
        else:
            filename = "678Tweets"       

        with open(filename, "r") as f:
            return json.load(f)
