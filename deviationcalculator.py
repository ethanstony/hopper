import numpy as np
import matplotlib.pyplot as plt
import math


def sample(sigma, slant=0.05, start=0, end=365, h=1):
    rng = np.random.default_rng()

    steps = int((end - start) / h + 1)
    mu = 1 + slant

    x = np.linspace(start, end, steps)
    y = [1]
    dis = rng.normal(mu, sigma, steps - 1)

    for ii in range(len(x) - 1):
        if (y[ii] > 0):
            q = y[ii] * dis[ii]
        else:
            q = slant

        if (q > 0):
            y.append(q)
        else:
            y.append(0)

    return x, y

def movingAvgCalc(val):
    window_size = 3
    i = 0
    moving_averages = []
    while i < len(val) - window_size + 1:
        window = val[i: i + window_size]
        window_average = round(sum(window) / window_size, 2)
        moving_averages.append(window_average)
        i += 1

    return moving_averages

def stdDevCalc(values):
    valTotal = sum(values)
    n = len(values)
    average = movingAvgCalc(values)
    total = 0

    for i in range(0, n):
        if i < len(average):
            total += (values[i] - average[i]) ** 2
    return math.sqrt(total / (n - 1))

def timeFramesDeviation(begin, end, xGraph, yGraph):
    values = []
    begin = int(begin)
    end = int(end)
    for i in range(begin, end):
        values.append(yGraph[i])
    return stdDevCalc(values)

def weekVolatility(xGraph, yGraph):
    return timeFramesDeviation(len(xGraph) - 7, len(xGraph), xGraph, yGraph)

def monthVolatility(xGraph, yGraph):
    return timeFramesDeviation(len(xGraph) - 30, len(xGraph), xGraph, yGraph)

def yearVolatility(xGraph, yGraph):
    return timeFramesDeviation(len(xGraph) - 180, len(xGraph), xGraph, yGraph)

#Test that looks at the data. Not necessary
sd = .3
err = 0
sde = 0
for ii in range(1):
    xs, ys = sample(sd)
    sde = timeFramesDeviation(0, len(xs) - 1, xs, ys)



    plt.plot(xs, ys)
    plt.plot(xs[1:-1], movingAvgCalc(ys))



    print("Standard Deviation: ", sde)
    print("Week Volatility: ", weekVolatility(xs, ys))
    print("Month Volatility: ", monthVolatility(xs, ys))
    print("Year Volatility: ", yearVolatility(xs, ys))
plt.show()