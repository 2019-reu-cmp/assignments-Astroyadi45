import numpy as np
import matplotlib.pyplot as plt

time,spots=np.loadtxt('sunspots.tsv',unpack=True)

plt.plot(time,spots,'.k')
plt.xlabel('Time')
plt.ylabel('# of Sunspots')
plt.grid(True)
#plt.show()

def moving_average(a,win):
    ones = np.ones((1,win))/win
    m=ones[0,:]
    sma = np.convolve(a,m,'same')
    return sma
mov_av=moving_average(spots,5)
plt.plot(time,mov_av,'-b')
plt.show()
        
