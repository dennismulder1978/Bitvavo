from Secret import const
from python_bitvavo_api.bitvavo import Bitvavo
import datetime

bitvavo = Bitvavo({
  'APIKEY': const.api_key,
  'APISECRET': const.api_secret,
  'RESTURL': 'https://api.bitvavo.com/v2',
  'WSURL': 'wss://ws.bitvavo.com/v2/',
  'ACCESSWINDOW': 10000,
  'DEBUGGING': False
})

def t(t:float):
  return datetime.datetime.fromtimestamp(t/1000)

def get_balance(symbol: str):
  try:
    return float(bitvavo.balance({"symbol": str.upper(symbol)})[0]['available'])
  except Exception:
    return Exception

def get_price(symbol: str):
  pair = str.upper(symbol) + '-EUR'
  try:
    return float(bitvavo.tickerPrice({"market": pair})['price'])
  except Exception:
    return Exception


def moving_avarages(symbol: str, length: int, time_type):
  pair = str.upper(symbol) + '-EUR'
  resp = bitvavo.candles(pair, time_type, {})
  temp = float(0)
  for j in range(1,length+1):
    temp += float(resp[j][4])
  return temp/length


def log(stringer: str, name: str):
  try:
      open(f'log/{name}.csv')
  except FileNotFoundError:
      with open(f'log/{name}.csv', 'w') as g:
          g.write('Action,' +
                  'Pair,' +
                  'Amount,' +
                  'Error,' +
                  'DateTime\n')
          g.close()
  with open(f'log/{name}.csv', 'a') as f:
      f.write(stringer + ',' + datetime.datetime.now() + '\n')
      f.close()
  return


def trade_market_order(symbol: str, action: str, amount):
  pair = str.upper(symbol) + '-EUR'
  try:
    bitvavo.placeOrder(pair, action, 'market', {'amount': amount})
    return f'{pair},{action},{amount}'
  except Exception:
    return Exception

