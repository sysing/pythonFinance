import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
    
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
    
    with open('sp500ticker.pickle','wb') as f:
        pickle.dump (tickers, f)
    
    print(tickers)
    
    return tickers

# save_sp500_tickers()

def get_data_from_yahoo(reload_sp500 = False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open('sp500ticker.pickle','rb') as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2016,12,31)

    for ticker in tickers[:50]: 
        print('Checking {} info'.format(ticker))
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            print('Grabbing ticker info')
            df = web.DataReader(ticker, 'robinhood', start, end )
            df.reset_index(inplace=True)
            df.drop(['symbol', 'interpolated', 'session'], axis=1, inplace=True)
            df.rename(index=str, columns={'close_price': 'Close', 
                                        'high_price': 'High',
                                        'low_price': 'Low',
                                        'open_price': 'Open',
                                        'volume': 'Volume',
                                        'begins_at': 'Date'}, inplace=True)
            df.set_index('Date', inplace=True)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))
        
    
get_data_from_yahoo()