import unittest
from web_app.get_dataframe import get_dataframe
class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_dates(self):
        self.assertIsNotNone(get_dataframe('2014-09-01', '2014-09-10'))

if __name__ == '__main__':
    unittest.main()