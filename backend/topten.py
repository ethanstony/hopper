import pandas as pd
from pandas import DataFrame
import json

def getTopTen():
    gainers = pd.read_html('https://finance.yahoo.com/gainers')[0].head(10)
    #convert fetched dataframe to json
    gainerjson = DataFrame.to_json(gainers, orient = "table")

    #convert applson json var to dict
    pythonObj = json.loads(gainerjson)['data']

    #create res dict with subdictionaries that have only 'Symbol' and '% Change' keys
    res = {}
    resIndex = 0
    for i in pythonObj:
        resObj = {}
        resObj['Symbol'] = i['Symbol']
        resObj['% Change'] = i['% Change']
        res[resIndex] = resObj
        resIndex += 1
    print(res)
    return res

getTopTen()
