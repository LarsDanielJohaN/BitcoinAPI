#Created by: Lars Daniel Johansson Nino, Data Science undegradaute student and economics Research Assistant at ITAM
#Last edited date: 29/10/22
#Purpose: Gather Pool distribution, Bitcoin price and Transaction fee´s for Bitcoin for research purposes
import requests as rq
import calendar as cd
import time as tm
import pandas as pd
import datetime

def main():
    """
    Specifics of data gathering of user history data are available at:
    https://docs.pool.btc.com/#/share?id=get-user-history-data
    """

    #sets initial start date as the 1st of july of 2013
    initDateTimeStamp = int((datetime.datetime(2003,7,1)).timestamp())
    print(initDateTimeStamp)

    urlPoolApi = 'https://pool.api.btc.com/v1/pool/share-history'
    paramsPool = {"dimension":"1d","start_ts":initDateTimeStamp,"count":500}

    temp = getJson(urlPoolApi,paramsPool)
    dataFrame = pd.DataFrame(getJson(urlPoolApi,paramsPool))


    print(dataFrame.keys())
    print(dataFrame.head())
    #print(temp)


#method that returns a generalized request from a desired API
def getJson(url,params):
    r = rq.get(url,params)
    return r.json();
main()
