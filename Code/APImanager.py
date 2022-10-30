#Created by: Lars Daniel Johansson Nino, Data Science undegradaute student and economics Research Assistant at ITAM
#Last edited date: 29/10/22
#Purpose: Gather Pool distribution, Bitcoin price and Transaction fee´s for Bitcoin for research purposes
import requests as rq
from bs4 import BeautifulSoup

def main():
    urlPoolApi = 'https://pool.api.btc.com/v1/pool/share-history'
    paramsPool = {"dimension":"1d","start_ts":1647838478,"count":20}
    #the url acceses BTC.com Pool API
    rPoolApi = rq.get(urlPoolApi,paramsPool)
    json_data = rPoolApi.json()
    print(json_data)



    
main()
