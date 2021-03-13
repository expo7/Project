from binance.websockets import BinanceSocketManager
import  csv
from utils import getVars
from binance.client import Client
client = Client(getVars.BINANCE_KEY, getVars.BINANCE_SECRET)
interval=Client.KLINE_INTERVAL_1HOUR
from binance.enums import *
# def process_message(msg):
#     print("message type: {}".format(msg['e']))
#     print(msg)
    # do something
    # do something
# #
# bm=BinanceSocketManager(client)
#
# bm.start_kline_socket('BNBBTC', process_message, interval=Client.KLINE_INTERVAL_1MINUTE)


# start aggregated trade websocket for BNBBTC
def process_message(msg):
    print(msg)
    # do something

# from binance.websockets import BinanceSocketManager
# 	candleSeries.update({
# 		time: candlestick.t / 1000,
# 		open: candlestick.o,
# 		high: candlestick.h,
# 		low: candlestick.l,
# 		close: candlestick.c
# 	})
# }

bm = BinanceSocketManager(client)
conn_key = bm.start_kline_socket('BNBBTC', process_message, interval=KLINE_INTERVAL_1MINUTE)
bm.start()
