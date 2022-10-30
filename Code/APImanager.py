#Created by: Lars Daniel Johansson Nino, Data Science undegradaute student and economics Research Assistant at ITAM
#Last edited date: 29/10/22
#Purpose: Gather Pool distribution, Bitcoin price and Transaction fee´s for Bitcoin for research purposes
import requests as rq
import calendar as cd
import time as tm

def main():
    urlPoolApi = 'https://pool.api.btc.com/v1/pool/share-history'
    paramsPool = {"dimension":"1d","start_ts":1647838478,"count":20}

    json_Pool = getJson(urlPoolApi,paramsPool)
    print(json_Pool)

#method that returns a generalized request from a desired API
def getJson(url,params):
    r = rq.get(url,params)
    return r.json();





main()
