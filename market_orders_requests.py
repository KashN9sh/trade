"""create order demo.

demonstrates:
- placing a market order
- placing a faulty market order
- usage of contrib.requests
- logging
"""
import json
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.positions as positions
import oandapyV20.endpoints.pricing as pricing
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.exceptions import V20Error
from exampleauth import exampleAuth
import logging
import time

accountID='101-004-9331170-001'
token='acbe0945e42a797eef080ea2e4f46d88-b32a040ee9d6394604d7661a406b91f7'
client = oandapyV20.API(access_token=token)
orderConf = [
    MarketOrderRequest(instrument="EUR_USD", units=100).data,
]

# client
api = API(access_token=token)

params ={
          "instruments": "EUR_USD"
        }
while True:
    r = pricing.PricingInfo(accountID=accountID, params=params)
    rv = api.request(r)
    print (r.response)
    '''for O in orderConf:
        r = orders.OrderCreate(accountID=accountID, data=O)
        print("processing : {}".format(r))
        print("===============================")
        print(r.data)
        try:
            response = api.request(r)
        except V20Error as e:
            print("V20Error: {}".format(e))
        else:
            print("Response: {}\n{}".format(r.status_code,
                                            json.dumps(response, indent=2)))

        time.sleep(5)
        data ={
          "longUnits": "ALL"
        }
        r = positions.PositionClose(accountID=accountID, data=data,instrument="EUR_USD",)
        client.request(r)
        print (r.response)'''
