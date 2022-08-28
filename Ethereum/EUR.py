
import json
import requests

key = "https://api.binance.com/api/v3/ticker/price?symbol="

currencies = ["ETHEUR"]
j = 0

for i in currencies:

 url = key+currencies[j]
data = requests.get(url)
data = data.json()
j = j+1
print("Le prix de l'Ethereum est de",data['price'],"€")