import samplegen as sg #"import FILENAME" will import from the local file
import matplotlib.pyplot as plt
import numpy as np

def predict(x,y,length=4):
    rough, rc = np.polyfit(x[-100:-4:4],y[-100:-4:4],2,cov=True)
    med, mc = np.polyfit(x[-60:-4:2],y[-60:-4:2],2,cov=True)
    fine, fc = np.polyfit(x[-40:-4],y[-40:-4],2,cov=True)

    rc = np.sqrt(np.diag(rc))
    mc = np.sqrt(np.diag(mc))
    fc = np.sqrt(np.diag(fc))

    a=[]
    ac = []
    for i in range(len(rough)):
        a.append(0)
        ac.append(0)

    for i in range(len(rough)):
        a[i]=0
        a[i]+=rough[i]*rc[i]
        a[i]+=med[i]*mc[i]
        a[i]+=fine[i]*fc[i]
        a[i]/=(rc[i]+mc[i]+fc[i])
        ac[i]=np.sqrt(mc[i]**2+rc[i]**2+fc[i]**2)

    ypre = []
    for i in range(length, 0, -1):
        ypr = y[-length]
        for j in range(1,len(rough)):
            ypr += a[j]*(x[-length]**j-x[-i]**j)
        if (ypr < 0):
            ypr =0
        ypre.append(ypr)

    #uncertainties
    yerr = []
    yhigh = []
    ylow = []
    for i in range(length,0,-1):
        drift = 0
        for j in range(1,len(rough)):
            drift += ac[j]*(x[-length]**j-x[-i]**j)
        yerr.append(abs(drift))
        yhigh.append(ypre[-i]+yerr[length-i])
        if(ypre[-i]-yerr[length-i]<0):
            ylow.append(0)
        else:
            ylow.append(ypre[-i]-yerr[length-i])

    return ypre, yhigh, ylow

for i in range(5):
    xs, ys = sg.sample(.3)
    ypred, yhi, ylo = predict(xs, ys)
#    plt.plot(xs,ys)
#    plt.show()
    plt.plot(xs[-7:],ys[-7:])
    plt.plot(xs[-4:],ypred,color='red')
    plt.fill_between(xs[-4:],yhi,ylo,color = 'red',alpha=0.2)
    plt.show()

