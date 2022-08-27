from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
cmc = CoinMarketCapAPI('49ea16ef-e9e7-4d65-bb31-5e5244dd8226')
r = cmc.cryptocurrency_info(symbol='BTC')
print(r)