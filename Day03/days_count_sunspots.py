'''Counts how many days sunspots have been between low,high counts'''
import numpy as np

sunspot_counts=np.loadtxt('sunspots.txt',usecols=(1),unpack=True)
print(sunspot_counts)
    
def counts(low,high):
    num_days=0
    for i in sunspot_counts:
        if (i>=low) & (i<=high):
            num_days+=1
    return num_days
lower_bound= 30 ##
upper_bound= 75 ##
print('Days with sunspot counts within limits:',counts(lower_bound,upper_bound))
