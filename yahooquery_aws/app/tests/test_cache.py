# import unittest
# from yahooquery_aws.app.cache import Cache
# import pandas as pd
#
#
# class CacheTest(unittest.TestCase):
#
#     def test_has_latest_year_equals(self):
#         cache_mock = Cache(
#             pd.DataFrame([{'ticker': 'MSFT', 'latest_date': 2021}, {'ticker': 'AAPL', 'latest_date': 2020}])
#         )
#         self.assertEqual(True, cache_mock.cache_has_latest_year('MSFT', 2021))
#
#     def test_has_latest_year_less_than(self):
#         cache_mock = Cache(
#             pd.DataFrame([{'ticker': 'MSFT', 'latest_date': 2021}, {'ticker': 'AAPL', 'latest_date': 2020}])
#         )
#         self.assertEqual(True, cache_mock.cache_has_latest_year('MSFT', 2020))
#
#     def test_has_latest_year_greater_than(self):
#         cache_mock = Cache(
#             pd.DataFrame([{'ticker': 'MSFT', 'latest_date': 2021}, {'ticker': 'AAPL', 'latest_date': 2020}])
#         )
#         self.assertEqual(False, cache_mock.cache_has_latest_year('MSFT', 2022))
#
#     def test_update_failed_time_if_none(self):
#         cache_mock = Cache(
#             pd.DataFrame([{'ticker': 'MSFT', 'latest_date': 2021}, {'ticker': 'AAPL', 'latest_date': 2020}])
#         )
#         cache_mock.update_failed_time_for_ticker('JPM')
#         self.assertIsNone(cache_mock.cache.get('JPM'))
#
#     def test_update_failed_time(self):
#         cache_mock = Cache(
#             pd.DataFrame([{'ticker': 'MSFT', 'latest_date': 2021}, {'ticker': 'AAPL', 'latest_date': 2020}]))
#         cache_mock.update_failed_time_for_ticker('MSFT')
#         self.assertFalse(cache_mock.cache.get('MSFT').last_success)
