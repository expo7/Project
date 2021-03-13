import pandas as pd
import numpy
import time
import talib
from utils import plots
from talib import MA_Type
from talib.abstract import *
import numpy as np
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
RSI_OVERBOUGHT=75
RSI_OVERSOLD=30
cols=['T','O','H','L','C','V']
data=pd.read_csv('data/live.csv')
df=pd.DataFrame(data)
df.drop(df.columns[6:], axis=1,inplace=True)
df.columns=cols
df['EMA30']=EMA(df.C,90)
df['EMA20']=EMA(df.C,10)
df['EMA10']=EMA(df.C,5)
df['EMA200']=EMA(df.C,90)
df.loc[(df['EMA10'] >= df['EMA200']),'emaUptrend']=True
df.loc[(df['EMA10'] <= df['EMA200']),'emaDowntrend']=True
df['RSI']=talib.RSI(df.C)
df['upper'], df['middle'], df['lower'] = talib.BBANDS(df.C, matype=MA_Type.T3)
df['BBsellSig']=df.C>df.upper
df['BBbuySig']=df.C<df.lower
df['BBsellSig']=df.C>df.upper
df['rsiOversold']=df.RSI<RSI_OVERSOLD
df['rsiOverbought']=df.RSI>RSI_OVERBOUGHT
df['macd'],df["sig"],df['diff']=MACDFIX(df.C)
df.loc[(df['diff'] >=0),'macdBuy']=True
df.loc[(df['EMA20'] <= df['EMA30']) & (df['EMA10'] <= df['EMA20'])&(df['C'] <= df['EMA10']), 'EMAsellSig'] = True
df.loc[(df['EMA20'] >= df['EMA30']) & (df['EMA10'] >= df['EMA20'])&(df['C'] >= df['EMA10']), 'EMAbuySig'] = True

###BUY
df.loc[(df.emaUptrend & df.macdBuy),'BUY']=1
##SELL
df.loc[(df.emaDowntrend & df.macdBuy !=True),'SELL']=1
# df.fillna(value=True, method=None, axis=0, inplace=True, limit=None, downcast=None)
df['BUY'].fillna(0,inplace=True)
df['SELL'].fillna(0,inplace=True)



# print(df.SELL.iloc[len(df)-1])
if df.loc[len(df)-1].SELL==1:
    print('sell')
if df.loc[len(df)-1].BUY==1:
    print('buy')
print(current_time)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(df.loc[len(df)-1]['T'])))



# plots.plot(df)
