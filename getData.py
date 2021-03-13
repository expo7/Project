import  csv
from binance.client import Client
from utils import getVars, functions
import datetime

client = Client(getVars.BINANCE_KEY, getVars.BINANCE_SECRET)
INTERVAL=Client.KLINE_INTERVAL_1MINUTE
BACKTRADER_START,BINANCE_START=functions.convertdates(month=3, day=7, year=21)
BACKTRADER_START_END,BINANCE_END=functions.convertdates(month=3, day=12, year=21)
csvfile = open('data/live.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')
candlesticks = client.get_historical_klines("BTCUSDT", INTERVAL,BINANCE_START)
for candlestick in  candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)
print(f'{len(candlesticks)} candlesticks collected')
csvfile.close()
