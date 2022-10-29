#Created by: Lars Daniel Johansson Nino, Data Science undegradaute student and economics Research Assistant at ITAM
#Last edited date: 29/10/22
#Purpose: Gather Pool distribution, Bitcoin price and Transaction fee´s for Bitcoin for research purposes
import requests as rq
url = 'pending'
r = rq.get(url)
json_data = r.json()
for key, value in json_data.items()
    print(key + ' ',value)
