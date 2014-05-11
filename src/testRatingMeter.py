from RatingMeter import *
from MeasureViewer import *
from gui import HardcodedTVShow
import unittest

class TestRatingMeter(unittest.TestCase):

    def test_create(self):
        rm = RatingMeter(HardcodedTVShow())
        self.assertNotEqual(rm, None)

    def test_tvshow_title(self):
        rm = RatingMeter(HardcodedTVShow())
        self.assertEqual(rm.getTvShow().title(), "The Null Show")

if __name__ == '__main__':
    unittest.main()
