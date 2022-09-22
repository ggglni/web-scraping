from email import header
import requests
from datetime import datetime
from dateutil import parser
import time

ticker = input('Enter the ticker of your stock:')
from_date = input('Enter start date in yyyy/mm/dd format:')
to_date = input('Enter end date in yyyy/mm/dd format:')
#we take the input date, then we have to convert it into date(with parser from dateutile), then into epoch (.timestamp()), then into an int
start = int(parser.parse(from_date).timestamp())
end=int(parser.parse(to_date).timestamp())


url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={start}&period2={end}&interval=1d&events=history&includeAdjustedClose=true'
#time here is epoch - seconds from 01-01-1970

headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

content = str(requests.get(url, headers=headers).content)

with open(f'{ticker}.csv','w') as coin:
    coin.write(content)


