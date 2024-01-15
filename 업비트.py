import math
import ccxt
print(math.sqrt(25))

bithumb = ccxt.bithumb()
market = bithumb.load_markets()

print(market.keys())
print(len(market))