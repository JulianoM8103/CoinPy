
  from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

  cmc = CoinMarketCapAPI('{YOUR_API_KEY}')
  
  r = cmc.cryptocurrency_info(symbol='BTC')

  do_something(r.data)