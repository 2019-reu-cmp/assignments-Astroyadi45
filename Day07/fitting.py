#!/usr/bin/env python3
"""fitting.py -- fits a two overlapping Gaussian peaks

Starting Code:
Mike Moran
mmoran0032@gmail.com
2016-06-28
Benjamin Rose
benjamin.rose@me.com
2017-06-20
Chris Seymour
seymour.16@nd.edu
2019-06-18
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import statistics as stat



def gaus(x, A, mu, sigma):
    """
    Returns y-value, for each given x, making a Gaussian.

    Parameters
    ----------
    x : numpy.array
        The input values for the Gaussian function. Similar to the x values 
        used in a plotting command.

    A : float
        Maximum value of the Gaussian.

    mu : float
        Location (along x-axis) for the center of the Gaussian. Maybe outside 
        the range of `x`.

    sigma : float
        Width of the Gaussian.

    Return
    ------
    numpy.array
        A y-value (in a Gaussian shape) for each `x` given.
    """
    return A * np.exp(-(x - mu)**2/(2 * sigma**2))


def fitter(x, A0, mu0, sigma0, A1, mu1, sigma1):
    """
    Function to fit to the data. Two Gaussians that... 
    """
    global one_gaus
    global two_gaus
    
    one_gaus=A0 * np.exp(-(x - mu0)**2/(2 * sigma0**2))
    two_gaus=A1 * np.exp(-(x - mu1)**2/(2 * sigma1**2))
    gaus_fit=one_gaus+two_gaus
    return gaus_fit

bins, counts = np.loadtxt('two_peaks.txt', unpack=True)
#One gaussian
##param,_= curve_fit(gaus,bins,counts) # fitting method
##plt.scatter(bins, counts)
##plt.plot(bins, gaus(bins, *param))
##plt.show()


#Double gaussian
param,_= curve_fit(fitter,bins,counts) # fitting method
x=np.linspace(0,30,100)
plt.scatter(bins, counts)
plt.plot(x, fitter(x, *param))
plt.plot(x,one_gaus)
plt.plot(x,two_gaus)
plt.show()
