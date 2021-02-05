import requests
import json
import time

url = "https://api.bittrex.com/api/v1.1/public/getticker?market=EUR-BTC"
INTERVAL = 1

prev_price = 0
while True:
    j = requests.get(url)
    data = json.loads(j.text)
    price = data['result']['Ask']
    if price != prev_price:
        print(str(price)+ " €")
        prev_price = price
    time.sleep(INTERVAL)