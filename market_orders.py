# -*- coding: utf-8 -*-
"""create order demo.

demonstrates:
- placing a market order
- placing a faulty market order
- logging
"""
import json
from oandapyV20 import API
import oandapyV20.endpoints.orders as orders
from oandapyV20.exceptions import V20Error
from exampleauth import exampleAuth
import logging

accountID='101-004-9331170-001'
token='acbe0945e42a797eef080ea2e4f46d88-b32a040ee9d6394604d7661a406b91f7'
orderConf = [
       # ok
       {
         "order": {
            "units": "100",
            "instrument": "EUR_USD",
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT"
          }
        },
       # wrong instrument, gives an error
       {
         "order": {
            "units": "100",
            "instrument": "UR_USD",
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT"
          }
        }
]

# client
api = API(access_token=token)

# create and process order requests
for O in orderConf:
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
