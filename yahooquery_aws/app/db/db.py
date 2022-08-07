import pandas as pd
import psycopg2
from ticker import Ticker


class DB:

    def __init__(self, conn):
        self.conn = conn
        # self.conn = psycopg2.connect("user={} host={} port={} password={}".format(username, host, port, password))

    def get_all_tickers(self) -> pd.DataFrame:
        return pd.read_sql("SELECT * FROM TICKERS", self.conn,
                           parse_dates=['last_updated', 'last_queried'])

    def delete_old_and_add_new_data(self, delete_old_statement: str, insert_new_statement: str):
        cur = self.conn.cursor()
        cur.execute(delete_old_statement)
        cur.execute(insert_new_statement)
        self.conn.commit()

    def update_ticker(self, ticker: Ticker):
        statement = "UPDATE TICKERS SET LAST_UPDATED='{}', LAST_QUERIED='{}', LATEST_YEAR={} WHERE TICKER='{}'".format(
            str(ticker.last_updated),
            str(ticker.last_queried),
            ticker.latest_year,
            ticker.ticker
        )
        cur = self.conn.cursor()
        cur.execute(statement)
        self.conn.commit()

    def delete_ticker(self, ticker: str):
        statement = "DELETE FROM TICKERS WHERE TICKER = '{}'".format(ticker)
        cur = self.conn.cursor()
        cur.execute(statement)
        self.conn.commit()
