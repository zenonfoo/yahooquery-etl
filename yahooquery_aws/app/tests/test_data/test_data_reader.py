import pandas as pd
import json
import os
from dataclasses import dataclass
from typing import List, Callable
from transform import format_yahooquery_dataclass


@dataclass
class DummyTicker:
    symbols: List[str]
    income_statement: Callable[[], pd.DataFrame]
    balance_sheet: Callable[[], pd.DataFrame]
    cash_flow: Callable[[], pd.DataFrame]
    summary_detail: dict
    summary_profile: dict


def get_yahooquery_test_data_as_ticker():
    ticker = 'MSFT'
    current_file_directory = os.path.dirname(__file__)
    balance_sheet = pd.read_csv(current_file_directory + '/yahooquery_msft_balance_sheet.csv')
    income_statement = pd.read_csv(current_file_directory + '/yahooquery_msft_income_statement.csv')
    cash_flow = pd.read_csv(current_file_directory + '/yahooquery_msft_cash_flow.csv')

    balance_sheet['asOfDate'] = [pd.Timestamp(date) for date in balance_sheet['asOfDate']]
    income_statement['asOfDate'] = [pd.Timestamp(date) for date in income_statement['asOfDate']]
    cash_flow['asOfDate'] = [pd.Timestamp(date) for date in cash_flow['asOfDate']]

    with open(current_file_directory + '/yahooquery_msft_summary_detail.json', 'r') as fp:
        summary_detail = json.load(fp)

    with open(current_file_directory + '/yahooquery_msft_summary_profile.json', 'r') as fp:
        summary_profile = json.load(fp)

    return DummyTicker(
        [ticker],
        lambda: income_statement,
        lambda: balance_sheet,
        lambda: cash_flow,
        {ticker: summary_detail},
        {ticker: summary_profile}
    )


def get_yahooquery_test_data_as_yahooquery_dataclass():
    ticker = get_yahooquery_test_data_as_ticker()
    return format_yahooquery_dataclass(ticker, 'MSFT', 'Microsoft')
