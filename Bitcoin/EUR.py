import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
print(data["bpi"]["EUR"]["rate"])