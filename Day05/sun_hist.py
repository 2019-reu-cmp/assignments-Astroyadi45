import numpy as np
import matplotlib.pyplot as plt

time,spots=np.loadtxt('sunspots.tsv',unpack=True)
bins=200
plt.hist(spots,bins)
plt.xlim([0,250])
plt.show()
