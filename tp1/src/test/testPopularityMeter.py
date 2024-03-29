import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from PopularityMeter import *
from MeasureView import *
from PostsView import PostsView
from TVShow import Seis78TVShow

import unittest
import datetime

class TestPopularityMeter(unittest.TestCase):

    def setUp(self):
        self.initialDate = datetime.datetime.strptime("10/5/2014", '%d/%m/%Y').date()
        self.finalDate = datetime.datetime.strptime("11/5/2014", '%d/%m/%Y').date()
        self.pm = PopularityMeter(Seis78TVShow(),
                             self.initialDate,
                             self.finalDate,
                                  0)

    def test_create(self):
        self.assertNotEqual(self.pm, None)

    def test_tvshow_title(self):
        self.assertEqual(self.pm.getTVShow().getName(), "678")

    def test_has_no_observers(self):
        self.assertEqual(len(self.pm.getObservers()), len([]))

    def test_subcribe_observer(self):
        self.assertEqual(len(self.pm.getObservers()), len([]))
        pv = PostsView()
        self.pm.subscribe(pv)
        self.assertEqual(len(self.pm.getObservers()), 1)
        self.pm.unsubscribe(pv)
        self.assertEqual(len(self.pm.getObservers()), 0)

    def test_show_qposts(self):
        pv = PostsView()
        mv = MeasureView()

        self.pm.subscribe(pv)
        self.pm.subscribe(mv)
        self.pm.measure()
        for qpost in pv.getPosts():
            print("Qualified Post:")
            print(qpost.getSentiment())
            print(qpost.getContent())
            print()
        
        print("Medicion de Popularidad:")
        print(mv.getMeasure().getValue())
        
        self.assertEqual(len(pv.getPosts()), 0)
        pv.setSentimentFilter(['Neutro'])
        self.assertNotEqual(len(pv.getPosts()), 0)


if __name__ == '__main__':
    unittest.main()
