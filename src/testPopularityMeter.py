from PopularityMeter import *
from MeasureViewer import *
from gui import HardcodedTVShow
import unittest
import datetime

class TestPopularityMeter(unittest.TestCase):

    def setUp(self):
        self.initialDate = datetime.datetime.strptime("10/5/2014", '%d/%m/%Y').date()
        self.finalDate = datetime.datetime.strptime("11/5/2014", '%d/%m/%Y').date()

    def test_create(self):
        pm = PopularityMeter(HardcodedTVShow(), self.initialDate,
                             self.finalDate)
        self.assertNotEqual(pm, None)

    def test_tvshow_title():
        pm = PopularityMeter(HardcodedTVShow(), self.initialDate,
                             self.finalDate)
        self.assertEqual(pm.getTvShow().title(), "The Null Show")

if __name__ == '__main__':
    unittest.main()

