import math
import matplotlib
import yfinance

def stdDevCalc(values):
    valTotal = sum(values)
    n = len(values)
    average = valTotal / n
    total = 0
    for i in range(0, n):
        total += (values[i] - average) ** 2
        print(total)
    return math.sqrt(total / (n-1))

def timeFrames(begin, end):


print(stdDevCalc([5.0, 12.3, 15.0, 20.0]))