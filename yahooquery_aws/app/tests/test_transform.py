import unittest
from transform import format_yahooquery_dataclass
from tests.test_data.test_data_reader import get_yahooquery_test_data_as_ticker


class TransformTest(unittest.TestCase):

    def test_format_yahooquery_dataclass(self):
        test_data = get_yahooquery_test_data_as_ticker()
        expected_years = [2019, 2020, 2021]
        results = format_yahooquery_dataclass(test_data, test_data.symbols[0], 'Microsoft')

        for date in results.income_statement:
            self.assertTrue(date.year in expected_years)

        for date in results.balance_sheet:
            self.assertTrue(date.year in expected_years)

        for date in results.cash_flow:
            self.assertTrue(date.year in expected_years)
