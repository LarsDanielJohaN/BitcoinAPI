#Created by: Lars Daniel Johansson Nino, Data Science undegradaute student and economics Research Assistant at ITAM
#Last edited date: 29/10/22
#Purpose: Gather Pool distribution, Bitcoin price and Transaction fee´s for Bitcoin for research purposes
import requests as rq
import calendar as cd
import time as tm
import pandas as pd
import datetime

def main():
    #sets initial start date as the 1st of july of 2013
    initDateTimeStamp = int((datetime.datetime(2003,7,1)).timestamp())
    print(initDateTimeStamp)


    #works
    urlT = 'https://api.blockchain.info/charts/hash-rate?timespan=5weeks&rollingAverage=8hours&format=json'
    #hasnt worked yet
    urlP = 'https://api.blockchain.info/charts/pools?timespan=5days'
    temp = getJson(urlP)

    #dataFrame = pd.DataFrame('data': getJson(urlP))


    #print(dataFrame.keys())
    #print(dataFrame.head())
    print(temp)


#method that returns a generalized request from a desired API
def getJson(url):
    r = rq.get(url)
    return r.json();
main()
