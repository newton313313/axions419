# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 02:24:43 2022

@author: user
"""
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
T = 1
def cv(p,m):
    return 1*p*sqrt(m**2+p**2)
def eps_v(nf,n_0):
    return 1*(nf/n_0)**(2/3)*(T/1)
def eps_dm(x):
    return 0
def eps_ga1(x):
    return (x/10^8)**2.2
def eps_ga2(x):
    return (x/10^8)**4

print(eps_v(3,2))
a0 = []
a = 0
for i in range(10):
    a0.append(i)
    a = a+1
    #print(a)
print(a0)
sea = [1,2,3,4,5,6]
sea.append(10)
print("sea=",sea)
print("enum",list(enumerate(sea[:-1])))
print(sea[0],sea[1])
print(sea[-1])
print(list(enumerate(sea)))
print(list(enumerate(sea, start=2)))
print(1.81e-2,2/10**8)
print("end")
