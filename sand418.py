# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 20:41:38 2022

@author: user
"""
#import sympy as sy
from sympy.liealgebras.root_system import RootSystem
c = RootSystem("A4")
print(c.cartan_matrix())              
print(10)