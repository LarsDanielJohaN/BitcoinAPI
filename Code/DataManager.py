#Created by: Lars Daniel Johansson Nino, Data Science undegradaute student and economics Research Assistant at ITAM
#Last edited date: 1/11/22
#Purpose: Explore Pool distribution, Bitcoin price and Transaction fee´s for Bitcoin for research purposes
import calendar as cd
import time as tm
import pandas as pd
from datetime import datetime

def main():

    serious_25k_trial1 = pd.read_csv('serious_25k_trial1.csv').set_index('Unnamed: 0')
    print(serious_25k_trial1.head())
    print(serious_25k_trial1.tail())
    lastObs = serious_25k_trial1.loc[[3010]]
    firstObs = serious_25k_trial1.loc[[0]]
    print(serious_25k_trial1.columns)

    print("First observation")
    print("Date:",datetime.fromtimestamp(int(firstObs['Time'])))
    print(firstObs['BlockHash'])



    print("Last observation")
    print("Date:",datetime.fromtimestamp(int(lastObs['Time'])))
    print(lastObs['BlockHash'])

    print(serious_25k_trial1['BlockHash'])



main()
