import samplegen as sg #"import FILENAME" will import from the local file
import matplotlib.pyplot as plt

#Test that looks at the data. Not necessary
for ii in range(10):
    xs, ys = sg.sample(.3)
    plt.plot(xs,ys)
plt.show()
