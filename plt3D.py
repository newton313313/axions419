# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:01:32 2022

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
#(x, y, z)座標
x = np.random.rand(30)
y = np.random.rand(30)
z = np.random.rand(30)

fig = plt.figure()
ax = Axes3D(fig)

#散佈圖
ax.scatter3D(x, y, z, c= "red")

plt.show()
print("end")    