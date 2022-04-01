# coding=utf-8

import ccxt
# import ccxt.async_support as ccxt_async # link against the asynchronous version of ccxt
from config import (login_key,login_secret)

# 打印出ccxt支持的所有交易所
# print(ccxt.exchanges)

# hitbtc   = ccxt.hitbtc({'verbose': True})
# bitmex   = ccxt.bitmex()
# huobipro = ccxt.huobipro()

# 初始化交易所 方式一
# binance_exchange = ccxt.binance({
#     # 'apiKey': login_key,
#     # 'secret': login_secret,
#     'enableRateLimit': True,
#     'proxies': {
#         'http': 'http://127.0.0.1:1081',
#         'https': 'http://127.0.0.1:1081',
#     },
# })

# 初始化交易所 方式二
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': login_key,
    'secret': login_secret,
    'enableRateLimit': True,
    'proxies': {
        'http': 'http://127.0.0.1:1081',
        'https': 'http://127.0.0.1:1081',
    },
})

tickers_data=exchange.fetchTicker('BTC/USDT')

tickers_data = exchange.fetchTickers(['BTC/USDT', 'ETH/USDT'])
print(exchange.id, tickers_data)

print (exchange.fetch_balance())
