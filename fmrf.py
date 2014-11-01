#!/usr/bin/env python
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Computer Modern Roman'
fsize = 32

import io
import scipy.optimize


def fano(x,*p):
    # Fit to FMR measurement
    # p[0]: A
    # p[1]: Hr
    # p[2]: dH
    # p[3]: theta
    # p[4]: m
    # p[5]: offset
    return((p[0]/((x-p[1])**2 + p[2]**2))*((x-p[1])*np.cos(p[3]) + p[2]*np.sin(p[3])) + p[4]*x + p[5])

# Comma -> Decimal
r = open('test.dat').read().replace(',','.')
# Load data
data = np.loadtxt(io.StringIO(r), unpack = True)

field = data[0]
Kerr = data[1]

#p, cov = scipy.optimize.curve_fit(func, x_data, y_data, p0=p_guess, sigma=y_sigma, maxfev=100*(len(x_data)+1))
p, pcvo = scipy.optimize.curve_fit(fano, field, Kerr, p0=[0,0,1,0,0,0])
punc = 100*np.sqrt(np.diagonal(pcvo))/abs(p)

plt.figure(1, figsize = (12,9))
plt.title('Data Fit', fontsize = fsize)
plt.xlabel(r'H', fontsize = fsize, labelpad = 20)
plt.ylabel(r'Kerr', fontsize = fsize, labelpad = 20)

plt.minorticks_on()
plt.tick_params(labelsize = fsize, which = 'both', right = 'off', top = 'off', pad = -10)
plt.tick_params(which = 'major', direction = 'out', length = 8, width = 3)
plt.tick_params(which = 'minor', direction = 'out', length = 5, width = 2)

plt.plot(field, Kerr, 'o')
plt.plot(field, fano(field,*p), lw = 2)