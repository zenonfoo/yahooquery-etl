import sqlite3
import pandas as pd
from typing import List


def get_duplicates() -> List[str]:
    conn = sqlite3.connect('yahooquery_aws/financial_data_yahooquery.db')
    tickers = list(pd.read_sql('SELECT * FROM TICKERS', conn)['ticker'])
    conn.close()
    counter = {}
    for ticker in tickers:
        if ticker in counter.keys():
            counter[ticker] += 1
        else:
            counter[ticker] = 1
    results = []
    for k, v in counter.items():
        if v > 1:
            results.append(k)

    return results

check = get_duplicates()