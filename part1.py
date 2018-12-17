import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

df = web.DataReader('CNP', 'robinhood', start, end)
df.reset_index(inplace=True)
df.drop(['symbol', 'interpolated', 'session'], axis=1, inplace=True)
df.rename(index=str, columns={'close_price': 'Close', 
                             'high_price': 'High',
                             'low_price': 'Low',
                             'open_price': 'Open',
                             'volume': 'Volume',
                             'begins_at': 'Date'}, inplace=True)
df.set_index('Date', inplace=True)

print(df.head())