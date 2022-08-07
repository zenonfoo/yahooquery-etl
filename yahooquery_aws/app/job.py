import time
import db.sql_statement_constructors as sql

from db.db import DB
from fetch_data import get_data_from_yahooquery
from transform import format_yahooquery_dataclass
from yahooquery_data_helper import get_latest_year_from_yahooquery_dataclass, get_years_from_yahooquery_dataclass
from config import table_name
from typing import List
from ticker import Ticker


class Job:

    def __init__(self, tickers: List[Ticker], db: DB):
        self.ticker_metadata = sorted(tickers, key=lambda x: x.last_queried)
        self.db = db

    def query_and_update(self, ticker_metadata: Ticker):
        ticker = ticker_metadata.ticker
        yahooquery_data = get_data_from_yahooquery(ticker)
        if yahooquery_data is not None:
            try:
                ticker_metadata.update_last_queried()

                # process
                formatted_yahooquery_data = format_yahooquery_dataclass(yahooquery_data, ticker_metadata.ticker,
                                                                        ticker_metadata.name)
                latest_year = get_latest_year_from_yahooquery_dataclass(formatted_yahooquery_data)
                years = get_years_from_yahooquery_dataclass(formatted_yahooquery_data)

                # statements
                delete_statement = sql.delete_for_ticker_and_year_statement_constructor(table_name, ticker, years)
                insert_statement = sql.convert_yahooquery_financial_statement_data_to_sql_insert_statement(
                    formatted_yahooquery_data, table_name)
                delete_metadata = sql.get_delete_sql_statement_for_ticker(ticker, 'metadata')
                insert_metadata = sql.convert_metadata_to_insert_statement(formatted_yahooquery_data.metadata,
                                                                           'metadata')
                # save data
                self.db.delete_old_and_add_new_data(delete_statement, insert_statement)
                self.db.delete_old_and_add_new_data(delete_metadata, insert_metadata)

                ticker_metadata.update_last_updated()
                ticker_metadata.update_latest_year(latest_year)

                self.db.update_ticker(ticker_metadata)
            except Exception as e:
                if str(e) == 'string indices must be integers':
                    self.db.delete_ticker(ticker_metadata.ticker)
                else:
                    print(ticker_metadata.ticker)
                    print(e)

    def run(self) -> None:
        while True:
            for ticker in self.ticker_metadata:
                self.query_and_update(ticker)
                time.sleep(5)
