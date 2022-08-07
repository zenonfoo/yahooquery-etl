from typing import List

import pandas as pd
from yahooquery import Ticker
from dataclasses import dataclass
import ticker


@dataclass
class YahooqueryData:
    ticker: str
    income_statement: pd.DataFrame
    balance_sheet: pd.DataFrame
    cash_flow: pd.DataFrame
    metadata: dict


metadata_key_names = [
    'city',
    'state',
    'zip',
    'country',
    'industry',
    'sector',
    'longBusinessSummary',
    'fullTimeEmployees',
    'dividendYield',
    'fiveYearAvgDividendYield',
    'trailingPE',
    'forwardPE',
    'marketCap',
    'currency',
    'ticker',
    'name'
]

metadata_key_names_to_be_number = [
    'fullTimeEmployees',
    'dividendYield',
    'fiveYearAvgDividendYield',
    'trailingPE',
    'forwardPE',
    'marketCap',
]


def convert_str_none(metadata: dict):
    return {k: '-' if v is None and k not in metadata_key_names_to_be_number else v for k, v in metadata.items()}


def remove_odd_currency_code(statement: pd.DataFrame) -> pd.DataFrame:
    currency_dict = {}
    for currency in statement['currencyCode']:
        if currency in currency_dict.keys():
            currency_dict[currency] += 1
        else:
            currency_dict[currency] = 1
    most_common_currency = None
    most_common_currency_count = 0
    for k, v in currency_dict.items():
        if v > most_common_currency_count:
            most_common_currency = k
            most_common_currency_count = v
    return statement[statement['currencyCode'] == most_common_currency]


def format_statement(statement: pd.DataFrame) -> pd.DataFrame:
    odd_currency_code_removed = remove_odd_currency_code(statement)
    twelve_month_data = odd_currency_code_removed[odd_currency_code_removed['periodType'] == '12M']
    twelve_month_data.index = twelve_month_data.asOfDate
    new_twelve_month_data = twelve_month_data.drop(['asOfDate', 'periodType', 'currencyCode'], axis=1)
    return new_twelve_month_data.transpose()


def format_yahooquery_dataclass(data: Ticker, ticker_name: str, name: str):
    ticker = data.symbols[0]
    summary_profile = data.summary_profile[ticker]
    summary_details = data.summary_detail[ticker]
    try:
        all_metadata = {**summary_profile, **summary_details, 'ticker': ticker_name, 'name': name}
    except:
        all_metadata = {'ticker': ticker_name, 'name': name}

    wanted_metadata = {k: all_metadata.get(k) for k in metadata_key_names}
    processed_metadata = convert_str_none(wanted_metadata)
    formatted_income_statement = format_statement(data.income_statement())
    formatted_balance_sheet = format_statement(data.balance_sheet())
    formatted_cash_flow = format_statement(data.cash_flow())
    return YahooqueryData(
        ticker,
        formatted_income_statement,
        formatted_balance_sheet,
        formatted_cash_flow,
        processed_metadata
    )


def convert_tickers_df_to_list_of_tickers_domain(tickers: pd.DataFrame) -> List[ticker.Ticker]:
    results = []
    for i in range(tickers.shape[0]):
        t = tickers.iloc[i]
        results.append(ticker.Ticker(
            t.ticker,
            t['name'],
            t.last_updated,
            t.last_queried,
            t.latest_year
        ))
    return results
