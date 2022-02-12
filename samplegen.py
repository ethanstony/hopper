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
        if (y[ii]>0):
            q=y[ii]*dis[ii]
        else:
            q=slant

        if(q>0):
            y.append(q)
        else:
            y.append(0)

    return x, y

#Test that looks at the data. Not necessary
for ii in range(10):
    xs, ys = sample(.3)
    plt.plot(xs,ys)
plt.show()
