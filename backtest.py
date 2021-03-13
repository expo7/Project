from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
from s import RSI
import backtrader as bt
import backtrader.indicators as btind
import backtrader.feeds as btfeeds
import backtrader
import backtrader.analyzers as btanalyzers
start = "1 Jan, 2020"
end = "5 Mar, 2021"
fromdate = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d')
todate = datetime.datetime.strptime('2021-03-5', '%Y-%m-%d')
if __name__ == '__main__':
    # Create a cerebro entitys
    cerebro = bt.Cerebro()

    # Add a strategy
    cerebro.addstrategy(RSI)
    # Create a Data Feed
    data = bt.feeds.GenericCSVData(dataname='2020_15minutes.csv', dtformat=2,
                                   compression=15, timeframe=bt.TimeFrame.Minutes,
                                   fromdate=fromdate, todate=todate)
    cerebro.adddata(data)
    cerebro.broker.setcash(1000000.0)
    start = cerebro.broker.getvalue()
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    thestrats = cerebro.run()
    thestrat = thestrats[0]

    finish = cerebro.broker.getvalue()
    profit = finish-start
    print(f'profit:{int(profit)}')
    cerebro.plot()
