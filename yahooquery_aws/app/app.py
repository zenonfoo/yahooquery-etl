from db.db import DB
from job import Job
from transform import convert_tickers_df_to_list_of_tickers_domain
import sqlite3


def main():
    conn = sqlite3.connect('financial_data_yahooquery.db')
    db = DB(conn)
    tickers = db.get_all_tickers()
    tickers_domain = convert_tickers_df_to_list_of_tickers_domain(tickers)
    job = Job(tickers_domain, db)
    job.run()


if __name__ == "__main__":
    main()
