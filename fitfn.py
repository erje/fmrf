#!/usr/bin/env python
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Computer Modern Roman'
fsize = 32

def fano(x,*p):
    # Fit to FMR measurement
    # p[0]: A
    # p[1]: Hr
    # p[2]: dH
    # p[3]: theta
    # p[4]: m
    # p[5]: offset
    return((p[0]/((x-p[1])**2 + p[2]**2))*((x-p[1])*np.cos(p[3]) + p[2]*np.sin(p[3])) + p[4]*x + p[5])

phases = [0,90,180,270]

Hr = 100 #mT
dH = 3 #mT
A = 3
H = np.linspace(0, 200, 1000)
m = 0
offset = 0

plt.figure(1, figsize = (12,9))
plt.title('FMR Fit Function', fontsize = fsize)
plt.xlabel(r'$H$, mT', fontsize = fsize, labelpad = 20)
plt.ylabel(r'$\chi$', fontsize = fsize, labelpad = 20)

plt.minorticks_on()
plt.tick_params(labelsize = fsize, which = 'both', right = 'off', top = 'off', pad = -10)
plt.tick_params(which = 'major', direction = 'out', length = 8, width = 3)
plt.tick_params(which = 'minor', direction = 'out', length = 5, width = 2)

for i in phases:
    theta = np.deg2rad(i)
    plt.plot(H, fano(H, A, Hr, dH, theta, m, offset), lw=2, label=r'$\Theta = $ ' + str(i))

plt.legend(fontsize = fsize/1.5)
plt.tight_layout()
plt.show()