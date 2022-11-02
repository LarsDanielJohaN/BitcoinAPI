#Created by: Lars Daniel Johansson Nino, Data Science undegradaute student and economics Research Assistant at ITAM
#Last edited date: 29/10/22
#Purpose: Gather Pool distribution, Bitcoin price and Transaction fee´s for Bitcoin for research purposes
import requests as rq
import calendar as cd
import time as tm
import pandas as pd
import datetime

"""
Current progress
Using a blocks data, I´ve been able to access its first transaction hash.
"""


def main():


    """
    The following links were test links used to test the code
    """
    #works
    urlT = 'https://api.blockchain.info/charts/hash-rate?timespan=5weeks&rollingAverage=8hours&format=json'
    #works
    urlP = 'https://blockchain.info/q/hashrate'

    """
    Currently I intend to part from the following block, the hashTT variable is the hash of a block transaction which is
    being used to test the code.
    """
    block = "0000000000000bae09a7a393a8acded75aa67e46cb81f7acaa5ad94f9eacd103"
    hashTT = "5b09bbb8d3cb2f8d4edbcf30664419fb7c9deaeeb1f62cb432e7741c80dbe5ba"

    gatherInfoBlocks(block, 300)
    gatherInforTransaction(hashTT)



"""
In gatherInfoBlocks and gatherInforTransaction I want to beggin from a given block, colect the hash from its first transaction,
and finally gather its first adress repeating the process for a desired number of blocks.
This is being done to estimate Bitcoin´s hash-rate distribution inspired on blockchain.com´s methodology explained at:
https://www.blockchain.com/explorer/charts/pools
"""



def gatherInforTransaction(hash):
    url = rf'https://api.blockcypher.com/v1/btc/main/txs/{hash}?limit=50&includeHex=true'
    req = getJson(url)
    print("TRANSACTION")
    print(req.keys())


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
