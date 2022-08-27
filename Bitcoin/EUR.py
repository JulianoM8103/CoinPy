import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
bitcoinprice = (data["bpi"]["EUR"]["rate"])

print("Le prix du Bitcoin est actuellement de",bitcoinprice,"€")