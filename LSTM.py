# LSTM - Long Short Term Memory
# ML Stock Models don't often work is due to poor implementation/understanding
# LSTMs are one of the most widely used and successful ML financial algorithm
# when paired with the correct problems are datasets

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
#the above 2 lines sync matplotlib and pandas plotting functions

ticker = yf.Ticker("MSFT")
data = ticker.history(period = "15y", interval = "1d")

data.sort_values('Date', inplace=True, ascending=True)
print(data.head())

plt.figure(num=None, figsize=(15,6), dpi=80, facecolor='w', edgecolor='k')
data['Close'].plot()
plt.tight_layout()
plt.grid()
#plt.show()

df = data[['Close']].copy()
#split data into train and test
train, test = df.iloc[0:-200], df.iloc[-200:len(df)]
print(len(train), len(test))

train_max = train.max()
train_min = train.min()

#Normalize the dataframes
train = (train - train_min) / (train_max - train_min)
test  = (test - train_min) / (train_max - train_min)
