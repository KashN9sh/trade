import json
import datetime
import time
import oandapy as opy
import configparser
import pandas as pd
import numpy as np
import requests
import http.client as httplib
import urllib
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails
import oandapyV20.endpoints.orders as orders
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.orders as orders
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.exceptions import V20Error

accountID='101-004-9331170-001'
access_token='acbe0945e42a797eef080ea2e4f46d88-b32a040ee9d6394604d7661a406b91f7'

oanda = opy.API(environment="practice", access_token=access_token)

api = oandapyV20.API(access_token=access_token)
while True:
    response = oanda.get_prices(instruments="EUR_USD")
    prices = response.get("prices")
    asking_price = prices[0].get("ask")
    print(asking_price)

    EUR_USD_STOP_LOSS = asking_price+0.005
    EUR_USD_TAKE_PROFIT = asking_price-0.005

    mktOrder = MarketOrderRequest(
        instrument="EUR_USD",
        units=10000,
        takeProfitOnFill=TakeProfitDetails(price=EUR_USD_TAKE_PROFIT).data,
        stopLossOnFill=StopLossDetails(price=EUR_USD_STOP_LOSS).data)

# create the OrderCreate request
    r = orders.OrderCreate(accountID, data=mktOrder.data)
    try:
    # create the OrderCreate request
        rv = api.request(r)
    except oandapyV20.exceptions.V20Error as err:
        print(r.status_code, err)
    else:
        print(json.dumps(rv, indent=2))
