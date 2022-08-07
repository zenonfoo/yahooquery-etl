from typing import List
from transform import YahooqueryData
from dataclasses import dataclass
import pandas as pd
import math


@dataclass
class StatementSQLRow:
    ticker: str
    key: str
    value: float
    statement: str
    date: pd.Timestamp
    year: int


def delete_for_ticker_and_year_statement_constructor(table: str, ticker: str, years: List[int]) -> str:
    list_str = str(years).replace('[', '(').replace(']', ')')
    return "DELETE FROM {} WHERE TICKER = '{}' AND YEAR IN {}".format(table, ticker, list_str)


def convert_statement_to_sql_table_format(df: pd.DataFrame, statement: str, ticker: str) -> List[StatementSQLRow]:
    results = []
    key_names = df.index

    for k in key_names:
        row = df.loc[k]
        dates = row.index
        for d in dates:
            value = row.loc[d]
            results.append(StatementSQLRow(ticker, k, value, statement, d, d.year))

    return results


def get_all_rows_to_publish_to_sql(data: YahooqueryData) -> List[StatementSQLRow]:
    ticker = data.ticker
    income_statement_sql_rows = convert_statement_to_sql_table_format(data.income_statement, 'income_statement', ticker)
    balance_sheet_sql_rows = convert_statement_to_sql_table_format(data.balance_sheet, 'balance_sheet', ticker)
    cash_flow_sql_rows = convert_statement_to_sql_table_format(data.cash_flow, 'cash_flow', ticker)
    return income_statement_sql_rows + balance_sheet_sql_rows + cash_flow_sql_rows


def convert_sql_row_to_insert_values(sql_rows: List[StatementSQLRow]) -> str:
    list_of_values = [
        "('{}','{}',{},'{}','{}',{})".format(row.ticker, row.key, 'NULL' if math.isnan(row.value) else row.value,
                                             row.statement,
                                             row.date, row.year)
        for row in sql_rows]
    return ",".join(list_of_values)


def convert_yahooquery_financial_statement_data_to_sql_insert_statement(data: YahooqueryData, table: str) -> str:
    sql_rows = get_all_rows_to_publish_to_sql(data)
    values_sql_string = convert_sql_row_to_insert_values(sql_rows)
    return "INSERT INTO {} (ticker, key, value, statement, date, year) VALUES {}".format(table, values_sql_string)


def convert_metadata_to_insert_values(metadata: dict) -> str:
    result_str = "("
    for val in metadata.values():
        if type(val) == str:
            result_str += '"{}",'.format(val.replace('"', "'"))
        else:
            result_str += "{},".format(val if (type(val) == float or type(val) == int) and val is not None else 'NULL')
    result_str += ")"
    return result_str.replace(',)', ')')


def convert_metadata_to_insert_statement(metadata: dict, table_name: str) -> str:
    insert_values = convert_metadata_to_insert_values(metadata)
    return "INSERT INTO {} (city,state,zip,country,industry,sector," \
           "longBusinessSummary,fullTimeEmployees,dividendYield,fiveYearAvgDividendYield," \
           "trailingPE,forwardPE,marketCap,currency,ticker,name) VALUES {}".format(
        table_name, insert_values)


def get_delete_sql_statement_for_ticker(ticker: str, table_name: str) -> str:
    return "DELETE FROM {} WHERE ticker='{}'".format(table_name, ticker)
