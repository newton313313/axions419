# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Input constants 
m = 1 # mass (kg)
L = 1 # length (m)
b = 0.5 # damping value (kg/m^2-s)
g = 9.81 # gravity (m/s^2)
delta_t = 0.02 # time step size (seconds)
t_max = 15.0 # max sim time (seconds)
theta1_0 = np.pi/2 # initial angle (radians)
theta2_0 = 0 # initial angular velocity (rad/s)
theta_init = (theta1_0, theta2_0)
# Get timesteps
#print(type(t_max))
t = np.linspace(0, t_max, int(t_max/delta_t))

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
        next_theta2 = theta2[-1] - (b/(m*L**2) * theta2[-1] - g/L *
            np.sin(next_theta1)) * dt
        theta1.append(next_theta1)
        theta2.append(next_theta2)
    return np.stack([theta1, theta2]).T
#plotting
theta_vals_euler = euler_pendulum_sim(theta_init, t)
theta_vals_int = integrate.odeint(int_pendulum_sim, theta_init, t)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(t, theta_vals_euler)
#ax.plot(t, theta_vals_int)
plt.show()


print("end")

