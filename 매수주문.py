import ccxt
import pprint

with open("bithumb.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    api_secret = lines[1].strip()

exchange = ccxt.bithumb(config={
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True
    }
)

resp = exchange.create_limit_buy_order(
    symbol="BTC/KRW",
    amount=0.0001,
    price=61998000.0
)
pprint.pprint(resp)