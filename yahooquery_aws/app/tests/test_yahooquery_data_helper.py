from yahooquery_data_helper import get_latest_year_from_yahooquery_dataclass
import unittest
from tests.test_data.test_data_reader import get_yahooquery_test_data_as_yahooquery_dataclass


class YahooqueryDataHelperTest(unittest.TestCase):

    def test_get_latest_year_from_yahooquery_dataclass(self):
        yahooquery_data = get_yahooquery_test_data_as_yahooquery_dataclass()
        latest_year = get_latest_year_from_yahooquery_dataclass(yahooquery_data)
        self.assertEqual(2021, latest_year)

