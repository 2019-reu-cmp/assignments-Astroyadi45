import numpy as np
import matplotlib.pyplot as plt

time,spots=np.loadtxt('sunspots.tsv',unpack=True)

plt.plot(time,spots,'.k')
plt.xlabel('Time')
plt.ylabel('# of Sunspots')
plt.grid(True)
plt.show()

def moving_average(a,win):
    average=[]
    low=0
    up=win
    for i in range(len(a)):
        window=np.array(a[low:up])
        #sum_elem=np.sum(window)
        loc_aver=np.mean(window)
        np.append(average,loc_aver)
        low=low+win
        up=up+win
    return average
mov_av=moving_average(time,5)
plt.plot(time,mov_av,'.b')
plt.show()
        
