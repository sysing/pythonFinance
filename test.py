import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests
import matplotlib.pyplot as mpl
from matplotlib import style

style.use('ggplot')
df = pd.read_csv('spf_500_joined_closes.csv')
df.plot()
mpl.show()