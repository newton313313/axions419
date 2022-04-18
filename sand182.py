# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 23:54:23 2022

@author: user
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Input constants 
nf = 1 # 
n_0 = 1 # 
pfx = 1 #fermi momenta
pfn = 1 #fermi momenta of neutron
m_ax = 1 # mass of the axion

delta_t = 0.02 # time step size (seconds)
t_max = 15.0 # max sim time (seconds)

theta1_0 = np.pi/2 # initial temp
theta2_0 = 0 # initial dT/dt
theta_init = (theta1_0, theta2_0)
b=0.3
m=0.5
#Get timesteps
#print(type(t_max))
t = np.linspace(0, t_max, int(t_max/delta_t))
#functions
def cv(p,m):
    return 1*p*(m**2+p**2)**0.5
def sumcv(p1,p2,m0):
    return cv(p1,m0) + cv(p2,m0)
def eps_v(nf,x):
    return 1*(nf/n_0)**(2/3)*(x/1)**8
def eps_dm(x):
    return 0
def eps_ga1(x):
    return 1*(x/(10^8))**(2.2)
def eps_ga2(x):
    return 1*(x/10^8)**4

print(cv(1,1))
print(sumcv(1,1,1))