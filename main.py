from func import trade_market_order, get_balance, moving_avarages, get_price, log
import datetime


# balances en prices
balance_LUNA2 = get_balance('LUNA2')
balance_EURO = get_balance('EUR')
price_LUNA2 = get_price('LUNA2')

# MA's
ma6_LUNA2 = moving_avarages('LUNA2', 6, '15m')
ma18_LUNA2 = moving_avarages('LUNA2', 18, '15m')

print(balance_LUNA2)
print(balance_EURO)
print(ma6_LUNA2)
print(ma18_LUNA2)
print(price_LUNA2)


# LOG items: Action, Pair, Amount, Error, datetime
if (ma6_LUNA2 > ma18_LUNA2) & (balance_EURO > 1):
    print(trade_market_order('luna2', 'buy', round(0.99*(balance_EURO / price_LUNA2), 4)))

elif (ma6_LUNA2 < ma18_LUNA2) & (balance_LUNA2 > 1):
    print(trade_market_order('luna2', 'sell', balance_LUNA2))

else:
    log(f'Do nothing,LUNA2-EUR,0,none', 'log')
    print('Do nothing')
