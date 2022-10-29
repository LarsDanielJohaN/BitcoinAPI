#Created by: Lars Daniel Johansson Nino, Data Science undegradaute student and economics Research Assistant at ITAM
#Last edited date: 29/10/22
#Purpose: Gather Pool distribution, Bitcoin price and Transaction fee´s for Bitcoin for research purposes
import requests as rq


urlPoolApi = 'https://${pool.api.btc.com}/${v1}/${GET /account/address/update}'
#the url acceses BTC.com Pool API
rPoolApi = rq.get(urlPoolApi)
json_data = rPoolApi.json()
print(json_data.text())
