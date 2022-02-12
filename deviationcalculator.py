import numpy as np
import matplotlib.pyplot as plt
import math

def sample(sigma, slant=0.015):
    rng = np.random.default_rng()
    start = 0
    end = 1
    h = 0.01
    steps = int((end-start)/h+1)
    mu = 1 + slant

    x = np.linspace(start, end, steps)
    y = [1]
    dis =  rng.normal(mu,sigma,steps-1)
    
    for ii in range(len(x)-1):
        y.append(y[ii]*(dis[ii]))

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
    for i in range(len(xGraph)):
        if xGraph[i] >= begin and xGraph[i] <= end:
            values.append(yGraph[i])
    return stdDevCalc(values)


#Test that looks at the data. Not necessary
sd = .2
err = 0
sde = 0
for ii in range(10):
    xs, ys = sample(sd)
    sde = timeFramesDeviation(0.5, 0.8, xs, ys)
    print(sde)
    err = abs(sd - sde) / sd * 100
    print(err)
    plt.plot(xs, ys)
    plt.plot(xs[1:-1], movingAvgCalc(ys))
plt.show()
