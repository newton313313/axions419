# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:28:56 2022

@author: user
"""
from scipy import special
import matplotlib.pyplot as plt
import numpy as np
n = 6
m = 0.3*n
p_monic = special.hermite(n, monic=True)
p_monic(1)
p_monic(1)
x = np.linspace(-m, m, 400)
y = p_monic(x)
plt.plot(x, y)
plt.title("Monic Hermite polynomial")
plt.xlabel("x")
plt.ylabel("H_n(x)")
plt.show()
print("n=",n)
print("end")