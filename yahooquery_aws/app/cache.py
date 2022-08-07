# import pandas as pd
# from dataclasses import dataclass
# from datetime import datetime
#
#
# @dataclass
# class IndividualCacheData:
#     ticker: str
#     name: str
#     last_updated: datetime
#     last_queried: datetime
#     latest_year: int
#
#
# class Cache:
#
#     def __init__(self, stocks_with_latest_dates_df: pd.DataFrame):
#         self.cache: dict[str, IndividualCacheData] = {
#             item['ticker']: IndividualCacheData(item['latest_date'], datetime.min, datetime.min, True) for item in
#             stocks_with_latest_dates_df.to_dict(orient='records')}
#
#     def cache_has_latest_year(self, ticker: str, latest_year: int) -> bool:
#         current_individual_cache_data: IndividualCacheData = self.cache.get(ticker)
#         if current_individual_cache_data is None:
#             return False
#         if current_individual_cache_data.latest_year < latest_year:
#             return False
#         return True
#
#     def update_failed_time_for_ticker(self, ticker) -> None:
#         current_individual_cache_data: IndividualCacheData = self.cache.get(ticker)
#         if current_individual_cache_data is not None:
#             new_individual_cache_data = IndividualCacheData(
#                 current_individual_cache_data.latest_year,
#                 current_individual_cache_data.last_updated,
#                 datetime.utcnow(),
#                 False
#             )
#             self.cache[ticker] = new_individual_cache_data
#
#     def update_last_queried_time(self, ticker) -> None:
#         current_individual_cache_data: IndividualCacheData = self.cache.get(ticker)
#         if current_individual_cache_data is not None:
#             new_individual_cache_data = IndividualCacheData(
#                 current_individual_cache_data.latest_year,
#                 current_individual_cache_data.last_updated,
#                 datetime.utcnow(),
#                 True
#             )
#             self.cache[ticker] = new_individual_cache_data
#
#     def update_last_updated_time(self, ticker) -> None:
#         current_individual_cache_data: IndividualCacheData = self.cache.get(ticker)
#         if current_individual_cache_data is not None:
#             new_individual_cache_data = IndividualCacheData(
#                 current_individual_cache_data.latest_year,
#                 datetime.utcnow(),
#                 current_individual_cache_data.last_queried,
#                 True
#             )
#             self.cache[ticker] = new_individual_cache_data
