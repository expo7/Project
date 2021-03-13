from login import account
import robin_stocks.robinhood as rs
order=rs.order_buy_crypto_by_price('ETH',3)
print(order)
