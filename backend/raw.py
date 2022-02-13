import pandas as pd
from pandas import DataFrame
import yfinance as yf
from yahoofinancials import YahooFinancials
import time
from datetime import datetime
from datetime import timezone
from dateutil.relativedelta import relativedelta
import json

def sendRaw():
    
    pd.set_option("display.max_rows", None, "display.max_columns", None)

    #get start date (1 yr before currentDate)
    startDate = datetime.today() - relativedelta(days=365)

    #get current date in yyyy-mm-dd format
    currentDate = time.strftime("%Y-%m-%d")

    #get AAPL data from yahoofinance 
    aapl_df = yf.download('AAPL', 
                        start = startDate,
                        end=currentDate
    )

    #convert fetched dataframe to json
    applson = DataFrame.to_json(aapl_df, orient = "table")

    #convert applson json var to dict
    pythonObj = json.loads(applson)['data']
    
    #create res dict with subdictionaries that have only 'Date' and 'Close' keys
    res = {}
    resIndex = 0
    for i in pythonObj:
        resObj = {}
        resObj['Date'] = datetime.fromisoformat(i['Date'][:-1]).astimezone(timezone.utc).strftime('%Y-%m-%d')
        resObj['Close'] = i['Close']
        res[resIndex] = resObj
        resIndex += 1

    return res
