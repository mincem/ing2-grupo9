import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from RatingMeter import *
from MeasureView import *
from PostsView import PostsView
from TVShow import *

import unittest
import datetime

class TestRatingMeter(unittest.TestCase):

    def setUp(self):
        self.aDate = datetime.datetime.strptime("10/5/2014",
                                                '%d/%m/%Y').date()
        self.rm = RatingMeter(BailandoTVShow(), self.aDate)

    def test_create(self):
        self.assertNotEqual(self.rm, None)

    def test_tvshow_name(self):
        self.assertEqual(self.rm.getTVShow().getName(), 
                         "Bailando por un sueño")

    def test_has_no_observers(self):
        self.assertEqual(len(self.rm.getObservers()), len([]))

    def test_subcribe_observer(self):
        self.assertEqual(len(self.rm.getObservers()), len([]))
        pv = PostsView()
        self.rm.subscribe(pv)
        self.assertEqual(len(self.rm.getObservers()), 1)

    def test_show_qposts(self):
        pv = PostsView()
        mv = MeasureView()

        self.rm.subscribe(pv)
        self.rm.subscribe(mv)
        self.rm.measure()
        for qpost in pv.getPosts():
            print("Qualified Post:")
            print(qpost.getSentiment())
            print(qpost.getContent())
            print()
        
        print("Medicion de Rating:")
        print(mv.getMeasure().getValue())

        self.assertNotEqual(len(pv.getPosts()), 0)
        
if __name__ == '__main__':
    unittest.main()
