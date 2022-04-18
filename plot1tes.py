# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:25:04 2022

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi * 2, np.pi * 2, 200)
y = (np.sin(x))**3 + np.cos(3*x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(x, y)
plt.show()


print("end")