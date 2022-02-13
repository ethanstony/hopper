import samplegen as sg #"import FILENAME" will import from the local file
import matplotlib.pyplot as plt
import numpy as np

def predict(x,y,length=4,deg=1):
    hist = len(x)
    hop = int(len(x)/30)

    rough, rc = np.polyfit(x[::hop],y[::hop],deg,cov=True)
    med, mc = np.polyfit(x[-90::int(90/30)],y[-90::int(90/30)],deg,cov=True)
    fine, fc = np.polyfit(x[-30:],y[-30:],deg,cov=True)
    near, nc = np.polyfit(x[-7:],y[-7:],deg,cov=True)

    rc = np.sqrt(np.diag(rc))
    mc = np.sqrt(np.diag(mc))
    fc = np.sqrt(np.diag(fc))
    nc = np.sqrt(np.diag(nc))

    print(rough)
    print(med)
    print(fine)
    print(near)

    a=[]
    ac = []
    for i in range(deg+1):
        a.append(0)
        ac.append(0)
        a[i]=0
        a[i]+=rough[i]*rc[i]*(2/3)**2*(1/3)
        a[i]+=med[i]*mc[i]*(2/3)**3
        a[i]+=fine[i]*fc[i]*(2/3)**2
        a[i]+=near[i]*nc[i]*2/3
        a[i]/=(rc[i]*(2/3)**2*1/3+mc[i]*(2/3)**3+fc[i]*(2/3)**2+nc[i]*2/3)
        ac[i]=np.sqrt(rc[i]**2+mc[i]**2+fc[i]**2+nc[i]**2)
    print(ac)
    print(a)

#Make the actual prediction
    ypre = []
    for i in range(length):
        ypr = y[-1]
        for j in range(1,deg+1):
            ypr += a[j]*(x[-1]**j-(x[-1]+i)**j)
        if (ypr < 0):
            ypr =0
        ypre.append(ypr)

    #uncertainties
    yhigh = []
    ylow = []
    for i in range(length):
        drift = 0
        for j in range(1,deg+1):
            drift += ac[j]*(x[-1]**j-(x[-1]+i)**j)
        yhigh.append(ypre[i]+abs(drift))
        print(drift)
        if(ypre[i]-abs(drift)<0):
            ylow.append(0)
        else:
            ylow.append(ypre[i]-abs(drift))

    return ypre, yhigh, ylow

while(True):
    d = int(input())
    if(d==0):
        quit()
    xs, ys = sg.sample(.3)
    ypred, yhi, ylo = predict(xs[:-3], ys[:-3],deg=d)
    plt.plot(xs,ys)
    plt.show()
    plt.plot(xs[-7:],ys[-7:])
    plt.plot(xs[-4:],ypred,color='red')
    plt.fill_between(xs[-4:],yhi,ylo,color = 'red',alpha=0.2)
    plt.show()

