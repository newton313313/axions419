# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 01:52:03 2022

@author: user
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Input constants 
nf = 1 #average fermion number density in NS 
n_0 = 0.16e-45 # 
a = 0.5#?
pfx = 0.34*1.602e-10*(nf*a/n_0) #fermi momenta
pfn = 0.34*1.602e-10*(nf*(1-a)/n_0) #fermi momenta of neutron
mx = e-27#dark sector particle mass?
mn = 1.674e-27#neutron mass?
m_ax = 1.264e20 # mass of the axion? not known
gs = 1.85e10 #in SI
delta_t = 0.02 # time step size (seconds)
t_max = 15.0 # max sim time (seconds)

theta1_0 = np.pi/2 # initial temperature
theta2_0 = 0 # initial dT/dt
theta_init = (theta1_0, theta2_0)
ma = 0.079 *1.602e-10
kb= 1.38e-23
#Get timesteps
#print(type(t_max))
t = np.linspace(0, t_max, int(t_max/delta_t))
#functions
def cv(p,m):
    return (kb**2/3)*p*(m**2+p**2)**0.5
def sumcv(p1,p2,m1,m2,x):
    return (cv(p1,m1) + cv(p2,m2))*kb**2 *x /3
def eps_v(nf,x):
    return (1.81e-27)*(nf/n_0)**(2/3)*(x/1)**8
def eps_dm(x):
    return 0
def eps_ga1(x):
    return 1*(x/10**8)**(2.2)
def eps_ga2(x):
    return 1*(x/10**8)**4
print(sumcv(pfx,pfn,1,1,1))
def DT(x):
    return (-eps_v(1,1)-eps_ga1(1))#/(sumcv(pfx,pfn,1,1,x))
##
def int_axion(theta_init, t):
    theta_dot_1 = theta_init[1] #position
    theta_dot_2 = 1 #dT/dt
    return theta_dot_1, theta_dot_2
def euler_axion(theta_init, t):
    theta1 = [theta_init[0]]
    theta2 = [theta_init[1]]
    dt = t[1] - t[0]
    for i, t_ in enumerate(t[:-1]):
        next_theta1 = theta1[-1] + theta2[-1] * dt
        next_theta2 = theta2[-1] + DT(theta2[-1]) * dt
        theta1.append(next_theta1)
        theta2.append(next_theta2)
    return np.stack([theta1, theta2]).T #transpose
##
def int_pendulum_sim(theta_init, t, L=1, m=1, b=0, g=9.81):
    theta_dot_1 = theta_init[1] #position
    theta_dot_2 = -b/m*theta_init[1] - g/L*np.sin(theta_init[0]) #ang momen
    return theta_dot_1, theta_dot_2
def euler_pendulum_sim(theta_init, t, L=1, g=9.81):
    theta1 = [theta_init[0]]
    theta2 = [theta_init[1]]
    dt = t[1] - t[0]
    for i, t_ in enumerate(t[:-1]):
        next_theta1 = theta1[-1] + theta2[-1] * dt
        next_theta2 = theta2[-1] - (b/(m*L**2) * theta2[-1] + g/L *
            np.sin(next_theta1)) * dt
        theta1.append(next_theta1)
        theta2.append(next_theta2)
    return np.stack([theta1, theta2]).T
##
#plotting
#theta_vals_euler = euler_pendulum_sim(theta_init, t)
#theta_vals_int = integrate.odeint(int_pendulum_sim, theta_init, t)
theta_vals_euler = euler_axion(theta_init, t)
theta_vals_int = integrate.odeint(int_axion, theta_init, t)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(t, theta_vals_euler)
#ax.plot(t, theta_vals_euler)
#ax.plot(t, theta_vals_int)
plt.show()


print("end")