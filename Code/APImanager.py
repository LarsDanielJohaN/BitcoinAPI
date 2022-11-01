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
    block = "0000000000000bae09a7a393a8acded75aa67e46cb81f7acaa5ad94f9eacd103"
    hashT = "b6f6991d03df0e2e04dafffcd6bc418aac66049e2cd74b80f14ac86db1e3f0da"
    hashTT = "5b09bbb8d3cb2f8d4edbcf30664419fb7c9deaeeb1f62cb432e7741c80dbe5ba"

    gatherInfoBlocks(block, 300)
    gatherInforTransaction(hashTT)





def gatherInforTransaction(hash):
    url = rf'https://api.blockcypher.com/v1/btc/main/txs/{hash}?limit=50&includeHex=true'
    req = getJson(url)
    print(req.keys())
    #print(req['addresses'])

    print(req)


def gatherInfoBlocks(block, cant):
    url = rf"https://blockchain.info/rawblock/{block}"
    req = getJson(url)
    dataFrame = pd.DataFrame(req['tx'])
    print(req.keys())
    print(dataFrame.keys())
    print(dataFrame.head())
    print(dataFrame['hash'][0])


#method that returns a generalized request from a desired API
def getJson(url):
    r = rq.get(url)
    return r.json();
main()
