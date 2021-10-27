import requests

btc = requests.get("http://api.bithumb.com/public/ticker/").json()['data']
print(btc['opening_price'])