# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 05:10:31 2022

@author: user
"""

import scipy as sp
import pylab as plt
import numpy as np
from kuramoto0 import kuramoto

# Defining time array
t0, t1, dt = 0, 40, 0.01
T = np.arange(t0, t1, dt)

# Y0, W, K are initial phase, intrinsic freq and
# coupling K matrix respectively
Y0 = np.array([0, np.pi, 0])
W = np.array([28, 19, 11])

K1 = np.array([[  0, 0.2,  1.1],
               [0.5,   0, -0.7],
               [0.3, 0.9,    0]])

K2 = np.array([[   0, -0.5, 0.2],
               [-0.4,    0, 1.0],
               [ 0.8,  0.8,   0]])
K = np.dstack((K1, K2)).T

# Passing parameters as a dictionary
init_params = {'W':W, 'K':K, 'Y0':Y0}

# Running Kuramoto model
kuramoto = Kuramoto(init_params)
odePhi = kuramoto.solve(T)

# Computing phase dynamics
phaseDynamics = np.diff(odePhi)/dt

# Plotting response
nOsc = len(W)
for osc in range(nOsc):
    plt.subplot(nOsc, 1, 1+osc)
    plt.plot(T[:-1], phaseDynamics[osc])
    plt.ylabel("$\dot\phi_{%i}$" %(osc+1))
plt.show()
print("end")

