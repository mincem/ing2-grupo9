from RatingMeter import *
from MeasureView import *
from gui import HardcodedTVShow
from PostsView import PostsView

import unittest
import datetime

class TestRatingMeter(unittest.TestCase):

    def setUp(self):
        self.aDate = datetime.datetime.strptime("10/5/2014", '%d/%m/%Y').date()

    def test_create(self):
        rm = RatingMeter(HardcodedTVShow(), self.aDate)
        self.assertNotEqual(rm, None)

    def test_tvshow_title(self):
        rm = RatingMeter(HardcodedTVShow(), self.aDate)
        self.assertEqual(rm.getTvShow().title(), "The Null Show")

    def test_has_no_observers(self):
        rm = RatingMeter(HardcodedTVShow(), self.aDate)
        self.assertEqual(len(rm.getObservers()), len([]))

    def test_subcribe_observer(self):
        rm = RatingMeter(HardcodedTVShow(), self.aDate)
        self.assertEqual(len(rm.getObservers()), len([]))
        pv = PostsView()
        rm.subscribe(pv)
        self.assertEqual(len(rm.getObservers()), 1)

    def test_show_qposts(self):
        rm = RatingMeter(HardcodedTVShow(), self.aDate)
        pv = PostsView()
        mv = MeasureView()

        rm.subscribe(pv)
        rm.subscribe(mv)
        rm.measure()
        for qpost in pv.getPosts():
            print("Qualified Post:")
            print(qpost.getSentiment())
            print(qpost.getContent())
        
        print("Medicion de Rating:")
        print(mv.getRating().getValue())

        self.assertNotEqual(len(pv.getPosts()), 0)
        
if __name__ == '__main__':
    unittest.main()
