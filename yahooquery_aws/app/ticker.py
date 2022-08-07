import pandas as pd


class Ticker:

    def __init__(self, ticker: str, name: str, last_updated: pd.Timestamp, last_queried: pd.Timestamp,
                 latest_year: int):
        self.ticker = ticker
        self.name = name
        self.last_updated = last_updated
        self.last_queried = last_queried
        self.latest_year = latest_year

    def has_latest_year(self, latest_year: int) -> bool:
        if self.latest_year < latest_year:
            return False
        return True

    def update_last_queried(self) -> None:
        self.last_queried = pd.Timestamp.utcnow()

    def update_last_updated(self) -> None:
        self.last_updated = pd.Timestamp.utcnow()

    def update_latest_year(self, latest_year: int) -> None:
        self.latest_year = latest_year
