import numpy as np
import matplotlib.pyplot as plt

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

#Test that looks at the data. Not necessary
for ii in range(10):
    xs, ys = sample(.2)
    plt.plot(xs,ys)
plt.show()
