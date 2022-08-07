import pandas as pd
import sqlite3
import os
from typing import List


def add_ticker(ticker: str, name: str):
    conn = sqlite3.connect('yahooquery_aws/financial_data_yahooquery.db')
    to_save = [{
        'ticker': ticker,
        'name': name,
        'last_updated': pd.Timestamp('2000-01-01 00:00:00.000000+0000'),
        'last_queried': pd.Timestamp('2000-01-01 00:00:00.000000+0000'),
        'latest_year': 0
    }]
    pd.DataFrame(to_save).to_sql('tickers', conn, if_exists='append', index=False)
    conn.close()


def add_tickers(tickers: List[dict]):
    conn = sqlite3.connect('yahooquery_aws/financial_data_yahooquery.db')
    to_save = []
    for ticker in tickers:
        to_save.append({
            'ticker': ticker['ticker'],
            'name': ticker['name'],
            'last_updated': pd.Timestamp('2000-01-01 00:00:00.000000+0000'),
            'last_queried': pd.Timestamp('2000-01-01 00:00:00.000000+0000'),
            'latest_year': 0
        })
    pd.DataFrame(to_save).to_sql('tickers', conn, if_exists='append', index=False)
    conn.close()


def read_ticker_csv(relative_directory: str) -> List[dict]:
    return pd.read_csv(os.getcwd() + relative_directory).to_dict(orient='records')


add_ticker('0240.HK', 'Build King Holdings Limited')
