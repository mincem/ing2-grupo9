from twython import Twython, TwythonError
from TVShow import *
import json
from time import gmtime, strftime
import datetime
import urllib

class TwitterAdapter:
    def __init__(self):
        self._APP_KEY = 'D0PYmI7UMWHyzISn4Z7hPx8Mc'
        self._APP_SECRET = 'NNPnwOereOGZhzDxYrRrgM7IvU8khzSW5zT4F2F8LKs5yBwJz1'

    def searchFrom(self, keyword, date):
        twitter = Twython(self._APP_KEY, self._APP_SECRET)
        auth = twitter.get_authentication_tokens()
        OAUTH_TOKEN = auth['oauth_token']
        OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

#        twitterFinal = Twython(self._APP_KEY, self._APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        sinceDate = date.strftime("%Y-%m-%d")


        query = keyword + ' since:' + sinceDate

        try:
            search_results = twitter.search(q=query,count=100)
        except TwythonError as e:
            print(e)

        return search_results

    def searchForDate(self, keyword, initialDate):
        twitter = Twython(self._APP_KEY, self._APP_SECRET)
        auth = twitter.get_authentication_tokens()
        OAUTH_TOKEN = auth['oauth_token']
        OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

        twitterFinal = Twython(self._APP_KEY, self._APP_SECRET,
                               OAUTH_TOKEN,
                               OAUTH_TOKEN_SECRET)

        sinceDate = initialDate.strftime("%Y-%m-%d")

        untilDate = initialDate + datetime.timedelta(days=1)

        #query = keyword + ' since:' + initialDate.strftime("%Y/%m/%d") + ' until:' + finalDate.strftime("%Y/%m/%d")
        query = keyword + ' since:' + sinceDate + ' until:' + untilDate

        try:
            search_results = twitter.search(q=query, count=100)
        except TwythonError as e:
            print(e)

        return search_results

    def fetchTweets(self, initialDate, finalDate, keywordCollection):
        twitter = Twython(self._APP_KEY, self._APP_SECRET)
        auth = twitter.get_authentication_tokens()
        OAUTH_TOKEN = auth['oauth_token']
        OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

        twitterFinal = Twython(self._APP_KEY, self._APP_SECRET, 
                               OAUTH_TOKEN, 
                               OAUTH_TOKEN_SECRET)

        sinceDate = initialDate.strftime("%Y-%m-%d")

        untilDate = finalDate.strftime("%Y-%m-%d")

        #query = keyword + ' since:' + initialDate.strftime("%Y/%m/%d") + ' until:' + finalDate.strftime("%Y/%m/%d")
        keyword = ' OR '.join(keywordCollection)
        keyword = urllib.parse.quote_plus(keyword)
        # print(keyword)
        query = keyword + ' since:' + sinceDate + ' until:' + untilDate

        # try:
        #     search_results = twitter.search(q=query, count=100)
        # except TwythonError as e:
        #     print(e)

        # return search_results

        # new method
        tweets                          =   []
        MAX_ATTEMPTS                    =   10
        COUNT_OF_TWEETS_TO_BE_FETCHED   =   2000
        t = 0

        for i in range(0,MAX_ATTEMPTS):
            if(COUNT_OF_TWEETS_TO_BE_FETCHED < t):
                break

            if (0 == i):
                results = twitter.search(q=query, count=100)
            else:
                # After the first call we should have max_id from result of previous call. Pass it in query.
                results = twitter.search(q=query, include_entities='true',max_id=next_max_id,count=100)

            t = t + len(results['statuses'])
            tweets.append(results)

            try:
                # Parse the data returned to get max_id to be passed in consequent call.
                next_results_url_params = results['search_metadata']['next_results']
                next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
            except:
                # No more next pages
                break

        return tweets

class HardcodedTwitter(TwitterAdapter):
    def __init__(self):
        super(HardcodedTwitter, self).__init__()

    def searchFrom(self, keyword, date):
        if any(keyword in s for s in
               BailandoTVShow().getKeywords()):
            filename = "bailandoTweets"
        else:
            filename = "678Tweets"

        with open(filename, "r") as f:
            return json.load(f)

    def fetchTweets(self, initialDate, finalDate, keywordCollection):
        if any(keywordCollection[0] in s for s in
               BailandoTVShow().getKeywords()):
            filename = "bailandoTweets"
        else:
            filename = "678Tweets"

        with open(filename, "r") as f:
            return json.load(f)
