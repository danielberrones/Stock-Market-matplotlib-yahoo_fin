import matplotlib.pyplot as plt
import pandas as pd
from yahoo_fin.stock_info import get_analysts_info
from yahoo_fin.stock_info import get_data
from yahoo_fin.stock_info import get_market_status

pd.set_option('display.max_rows', None)

ticker = "SPY"

def getData(ticker):
    '''Return ticker adjusted close value as int'''
    ticker = get_data(ticker)['adjclose']
    # ticker = get_data(ticker)
    # col = ticker.columns
    # print(ticker)
    # val = []
    val = [int(i) for i in ticker]
    # for i in ticker:
    #     print(i)
    return val

def main():
    # print(getData(ticker))
    xVal = getData(ticker)
    yVal = [y for y in range(len(xVal))]
    # print(d)
    # xVal = [380,2,2,3,660]
    # yVal = [100,200,300,400,500]
    # TODO: fix plot errors
    plt.plot(xVal, yVal)
    plt.show()

main()
