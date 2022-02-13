import pandas as pd
from pandas import DataFrame
import yfinance as yf
from yahoofinancials import YahooFinancials
import time
import datetime
import json

def sendRaw():
    
    pd.set_option("display.max_rows", None, "display.max_columns", None)

    startDate = datetime.datetime.now() - datetime.timedelta(days=365)
    print(startDate)

    #get current date in yyyy-mm-dd format
    currentDate = time.strftime("%Y-%m-%d")

    aapl_df = yf.download('AAPL', 
                        start = '2022-02-10',
                        end=currentDate
    )
    print(aapl_df)
    applson = DataFrame.to_json(aapl_df, orient = "table")
    #applson = aapl_df.Close.to_json(orient = "table")  
    #applsonson = pd.read_json(applson, orient="table") 
    # print(applson.index(0))
    return applson

# print(type(sendRaw()))
# print(sendRaw())
# data = json.load(sendRaw())

# Got string
# take string -> json

# Got to read json -> dict
with open('output.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))

    for i in data['data']:
        print("Name:", i['Date'])
        print("Close:", i['Close'])