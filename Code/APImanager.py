#Created by: Lars Daniel Johansson Nino, Data Science undegradaute student and economics Research Assistant at ITAM
#Last edited date: 1/11/22
#Purpose: Gather Pool distribution, Bitcoin price and Transaction fee´s for Bitcoin for research purposes
import requests as rq
import calendar as cd
import time as tm
import pandas as pd
import datetime
"""
Current progress
Using a blocks data, I´ve been able to access its first transaction hash and its associated addresses.
A problem, none the less, is that it stops when accesing its 3010th observation.

"""

def main():

    """
    Currently I intend to part from the following block, the hashTT variable is the hash of a block transaction which is
    being used to test the code.
    """
    block = "0000000000000bae09a7a393a8acded75aa67e46cb81f7acaa5ad94f9eacd103"
    hashTT = "5b09bbb8d3cb2f8d4edbcf30664419fb7c9deaeeb1f62cb432e7741c80dbe5ba"

    print("Working on it")
    data = gatherInfoBlocks(block, 25000)
    data.to_csv('serious_25k_trial1.csv')
    print(data.head())
    print(data.tail())

"""
In gatherInfoBlocks and gatherInforTransaction I want to beggin from a given block, colect the hash from its first transaction,
and finally gather its first adress repeating the process for a desired number of blocks.
This is being done to estimate Bitcoin´s hash-rate distribution inspired on blockchain.com´s methodology explained at:
https://www.blockchain.com/explorer/charts/pools
"""

def gatherInforTransaction(hash):
    url = rf"https://api.bitaps.com/btc/v1/blockchain/transaction/{hash}"
    req = getJson(url)

    #Utilizes this try except to return any colected data in spite of unexpected errors
    try:
        return [req['data']['vOut']['0']['address'],req['data']['blockHeight']]
    except:
        print("ErrorOcurred on gatherInforTransaction!")
        return ["Error!"]

#returns a pandas data frame with desired data
def gatherInfoBlocks(block, cant):
    finalDataFrame = pd.DataFrame({'TransactionAddress':[], 'TransactionHash':[],'Time':[],'BlockHeight':[],'BlockHash':[]})
    i = 0
    cont = True

    while(i<cant and cont):
        print(i)
        url = rf"https://blockchain.info/rawblock/{block}"
        #makes request to blockchain.info
        req = getJson(url)
        #converts into data frame temporarelly
        tempDataFrame = pd.DataFrame(req['tx'])
        #adds new observation
        inforTrans = gatherInforTransaction(tempDataFrame['hash'][0])

        #Utilizes this try except to return any colected data in spite of unexpected errors
        try:
            finalDataFrame.loc[len(finalDataFrame.index)] = [inforTrans[0],tempDataFrame['hash'][0],tempDataFrame['time'][0],inforTrans[1],block]
            #sets new block to be checked
            block = req['next_block'][0]
            #because of the API limit of a rate of 3 requests per 5 seconds, it makes a small pause
            tm.sleep(1.45)
            i+=1
        except:
            print("Error ocurred in gatherInfoBlocks!")
            cont = False

    return finalDataFrame

#method that returns a generalized request from a desired API
def getJson(url):
    try:
        r = rq.get(url)
        res = r.json();

    except:
        res = "Error!"
    return res;


def getJsonP(url,params):
    r = rq.get(url,params)
    return r.json();
main()
