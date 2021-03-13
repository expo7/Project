from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


import backtrader as bt
import backtrader.indicators as btind
import backtrader.feeds as btfeeds
import datetime  # For datetime objects


class RSI(bt.Strategy):
    alias = ('RSI')

    params = (
        # period for the fast Moving Average
        ('period', 15),
    )

    def __init__(self):
        self.rsi = btind.RSI(period=self.params.period)
        # self.macd = btind.MACD()
        # self.macd = btind.EMA(9) - btind.EMA(14)
        # self.signal = btind.EMA(14)
        self.sma = btind.SimpleMovingAverage(period=21)
        self.ema = btind.ExponentialMovingAverage(period=14)
        self.accDe=btind.AccDeOsc(period=14)

        self.close_over_sma = self.data.close > self.sma
        self.close_over_ema = self.data.close > self.ema
        self.sma_ema_diff = self.sma - self.ema

        self.buy_sig = bt.And(self.close_over_sma, self.close_over_ema, self.sma_ema_diff > 0)
        self.max_pos = 10
        self.overSold = self.rsi < 50
        self.overBought = self.rsi > 70
        self.oscSig=self.accDe>0
        self.buy_price = []
        self.sell_price = []
        self.buy_price = []
        self.sell_price = []
        self.ave_buy = 0
        self.ave_sell = 0

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print(
            f'${int(self.broker.get_cash())},POS:{self.position.size},{dt.isoformat()}')

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                # self.log('BUY EXECUTED, %.2f' % order.executed.price)
                self.buy_price.append(order.executed.price)
                self.ave_buy = sum(self.buy_price) / len(self.buy_price)
                self.log(f'BUY')
            elif order.issell():
                # self.log('SELL EXECUTED, %.2f' % order.executed.price)
                self.sell_price.append(order.executed.price)
                self.ave_sell = sum(self.sell_price) / len(self.sell_price)
                self.log(
                    f'SELL,PROFIT:{int(self.position.price-order.executed.price)}')

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None

    def next(self):
        if self.position.size>0:
            if not self.buy_sig and self.overBought and not self.oscSig:
                self.sell(size=1)

        if  self.position.size < 10 and self.buy_sig and self.oscSig and self.overSold:
            self.buy(size=1)
