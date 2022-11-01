#Created by: Lars Daniel Johansson Nino, Data Science undegradaute student and economics Research Assistant at ITAM
#Last edited date: 29/10/22
#Purpose: Gather Pool distribution, Bitcoin price and Transaction fee´s for Bitcoin for research purposes
import requests as rq
import calendar as cd
import time as tm
import pandas as pd
import datetime

"""
might be useful?
https://binance-docs.github.io/apidocs/spot/en/#hashrate-resale-list-user_data
"""


def main():
    #sets initial start date as the 1st of july of 2013
    initDateTimeStamp = int((datetime.datetime(2003,7,1)).timestamp())
    print(initDateTimeStamp)


    #works
    urlT = 'https://api.blockchain.info/charts/hash-rate?timespan=5weeks&rollingAverage=8hours&format=json'
    #works
    urlP = 'https://blockchain.info/q/hashrate'
    #FINALY WORKS!!!
    urlC = "https://api.blockchain.info/pools"
    #wasnt what I was looking for, lets try again
    urlD = "https://blockchain.info/rawblock/0000000000000bae09a7a393a8acded75aa67e46cb81f7acaa5ad94f9eacd103"
    temp = getJson(urlD)


    #talvez obtener el hash? y de esa forma lograr hacer una base de datos con los mas grandes?
    #dataFrame = pd.DataFrame(getJson(urlD))

    print(temp)
    #print(dataFrame.keys())
    #print(dataFrame.head())
    #print(temp)


#method that returns a generalized request from a desired API
def getJson(url):
    r = rq.get(url)
    return r.json();
main()
