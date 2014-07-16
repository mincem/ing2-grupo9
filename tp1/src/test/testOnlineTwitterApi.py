import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from TVShow import *
from TwitterAdapter import *
from Post import *

import unittest
import datetime


class TestOnlineTwitterApi(unittest.TestCase):
    def test_search_tweets(self):
        seis78 = Seis78TVShow()
        t = TwitterAdapter()
        date = datetime.datetime(2014, 7, 14, 21, 30, 00)
        print (seis78.getKeywords()[0])
        tweets = t.searchFrom(seis78.getKeywords()[0], date)

        for tweet in tweets['statuses']:
            print ('Tweet from @%s Date: %s' %
                   (tweet['user']['screen_name'].encode('utf-8'), 
                    tweet['created_at']))
            print (tweet['text'].encode('utf-8'), '\n')
        self.assertNotEqual(tweets, None)

if __name__ == '__main__':
    unittest.main()




















