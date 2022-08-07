from transform import YahooqueryData
import pandas as pd
from typing import List


def get_latest_year_from_yahooquery_dataclass(data: YahooqueryData) -> int:
    years: pd.Index[pd.Timestamp] = data.income_statement.columns
    return sorted(years, key=lambda x: x.year)[-1].year


def get_years_from_yahooquery_dataclass(data: YahooqueryData) -> List[int]:
    years: pd.Index[pd.Timestamp] = data.income_statement.columns
    return [year.year for year in years]
