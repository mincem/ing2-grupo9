from TVShow import *
from Twitter import *

import unittest
import datetime

class TestTwitter(unittest.TestCase):

    def test_create_show(self):
        seis78 = Seis78TVShow()
        self.assertEqual(seis78.getTitle(), "678")
        
        showmatch = BailandoTVShow()
        # print( showmatch.getAiringDays())
        # print(  showmatch.getTime())
        # print( showmatch.getHashtags() )

    def test_search_teewts(self):
        seis78 = Seis78TVShow()
        t = Twitter()
        tweets = t.searchFrom(seis78.getHashtags()[0], "2014-4-28")
        self.assertNotEqual(tweets, None) 

    def test_search_hardcoded_teewts_678(self):
        seis78 = Seis78TVShow()
        t = HardcodedTwitter()
        tweets = t.searchFrom(seis78.getHashtags()[0], 
                              "2014-4-28")
        self.assertNotEqual(tweets, None) 
        for tweet in tweets['statuses']:
            print ('Tweet from @%s Date: %s' %
                   (tweet['user']['screen_name'].encode('utf-8'), 
                    tweet['created_at']))
            print (tweet['text'].encode('utf-8'), '\n')


    def test_search_hardcoded_teewts_bailando(self):
        showmatch = BailandoTVShow()
        t = HardcodedTwitter()
        tweets = t.searchFrom(showmatch.getHashtags()[0], 
                              "2014-4-28")
        self.assertNotEqual(tweets, None) 
        # for tweet in tweets['statuses']:
        #     print ('Tweet from @%s Date: %s' %
        #            (tweet['user']['screen_name'].encode('utf-8'), 
        #             tweet['created_at']))
        #     print (tweet['text'].encode('utf-8'), '\n')
        
        
if __name__ == '__main__':
    unittest.main()
