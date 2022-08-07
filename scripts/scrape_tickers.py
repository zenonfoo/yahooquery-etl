from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/zenonfoo/Documents/Projects/chromedriver/chromedriver')

driver.get('https://www.londonstockexchange.com/indices/ftse-100/constituents/table')

results = []

page_source = check = driver.page_source
page_source_bs4 = BeautifulSoup(page_source)
table = page_source_bs4.find('table')
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    ticker = (cols[0].text + '.L').replace('..L', '.L')
    name = cols[1].text
    results.append({'name': name, 'ticker': ticker})
