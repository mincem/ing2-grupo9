from PopularityMeter import *
from MeasureView import *
from gui import HardcodedTVShow
from PostsView import PostsView

import unittest
import datetime

class TestPopularityMeter(unittest.TestCase):

    def setUp(self):
        self.initialDate = datetime.datetime.strptime("10/5/2014", '%d/%m/%Y').date()
        self.finalDate = datetime.datetime.strptime("11/5/2014", '%d/%m/%Y').date()

    def test_create(self):
        pm = PopularityMeter(HardcodedTVShow(),
                             self.initialDate,
                             self.finalDate)
        self.assertNotEqual(pm, None)

    def test_tvshow_title(self):
        pm = PopularityMeter(HardcodedTVShow(), 
                             self.initialDate,
                             self.finalDate)
        self.assertEqual(pm.getTvShow().title(), "The Null Show")

    def test_has_no_observers(self):
        pm = PopularityMeter(HardcodedTVShow(), 
                             self.initialDate,
                             self.finalDate)
      
        self.assertEqual(len(pm.getObservers()), len([]))

    def test_subcribe_observer(self):
        pm = PopularityMeter(HardcodedTVShow(), 
                             self.initialDate,
                             self.finalDate)
        self.assertEqual(len(pm.getObservers()), len([]))
        pv = PostsView()
        pm.subscribe(pv)
        self.assertEqual(len(pm.getObservers()), 1)
        pm.unsubscribe(pv)
        self.assertEqual(len(pm.getObservers()), 0)

if __name__ == '__main__':
    unittest.main()

