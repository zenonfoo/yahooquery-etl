from yahooquery import Ticker


def get_data_from_yahooquery(ticker: str) -> Ticker:
    try:
        data = Ticker(ticker, timeout=10, retry=2)
        return data
    except:
        return None
