#Created by: Lars Daniel Johansson Nino, Data Science undegradaute student and economics Research Assistant at ITAM
#Last edited date: 29/10/22
#Purpose: Gather Pool distribution, Bitcoin price and Transaction fee´s for Bitcoin for research purposes
import requests as rq
import calendar as cd
import time as tm
import pandas as pd

def main():

    """
    Specifics of data gathering of user history data are available at:
    https://docs.pool.btc.com/#/share?id=get-user-history-data
    """

    urlPoolApi = 'https://pool.api.btc.com/v1/pool/share-history'
    paramsPool = {"dimension":"1d","start_ts":1647838478,"count":20}

    dataFrame = pd.DataFrame(getJson(urlPoolApi,paramsPool))

    print(dataFrame.head())

#method that returns a generalized request from a desired API
def getJson(url,params):
    r = rq.get(url,params)
    return r.json();





main()
