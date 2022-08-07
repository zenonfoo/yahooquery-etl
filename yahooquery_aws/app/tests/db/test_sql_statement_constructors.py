import unittest
from db.sql_statement_constructors import \
    delete_for_ticker_and_year_statement_constructor, \
    convert_yahooquery_financial_statement_data_to_sql_insert_statement, get_all_rows_to_publish_to_sql, \
    convert_metadata_to_insert_statement
from yahooquery import Ticker
from transform import format_yahooquery_dataclass


class SQLStatementConstructorsTest(unittest.TestCase):

    def test_delete_for_ticker_and_year_statement_constructor(self):
        result = delete_for_ticker_and_year_statement_constructor('yearly_financial_statement', 'AAPL', [2020, 2021])
        self.assertEqual("DELETE FROM yearly_financial_statement WHERE TICKER = 'AAPL' AND YEAR IN (2020, 2021)",
                         result)

    def test_convert_yahooquery_financial_statement_data_to_sql_insert_statement(self):
        # Removes duplicated statement row caused by being presented in different currencies
        t = '2378.HK'
        ticker = Ticker(t)
        ticker_domain = format_yahooquery_dataclass(ticker, t, 'name')
        results = convert_yahooquery_financial_statement_data_to_sql_insert_statement(ticker_domain, '')
        self.assertIsNotNone(results)

    def test_convert_metadata_to_insert_statement(self):
        # Converts " to ' for strings as not to mess up string conversion
        t = '87001.HK'
        ticker = Ticker(t)
        ticker_domain = format_yahooquery_dataclass(ticker, t, 'name')
        results = convert_metadata_to_insert_statement(ticker_domain.metadata, '')
        self.assertIsNotNone(results)

    def test_convert_metadata_to_insert_statement(self):
        # Converts " to ' for strings as not to mess up string conversion
        t = 'PHAR'
        ticker = Ticker(t)
        ticker_domain = format_yahooquery_dataclass(ticker, t, 'name')
        results = convert_yahooquery_financial_statement_data_to_sql_insert_statement(ticker_domain, '')
        self.assertIsNotNone(results)
