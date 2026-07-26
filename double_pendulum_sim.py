import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# constants / parameters
g = 9.81 #m/s^2[down]
m1 = 1 #kg
m2 = 1 #kg
l1 = 1 #m
l2 = 2 #m
dt = 0.05 #delta time, the time between each step/drawing of the visualisation
t_max = 15 # maximum time for the simulation to run for

n_steps=int(t_max / dt) # number of frames per simulation

# starting conditions
theta1 = np.pi /3 #degrees # np.pi is numpy's approximation of pi
theta2 = np.pi/2 #degrees
av1 = 0 #av= angular vecocity of each mass in rad/s angular velocity is the change in angular displacement over the change in time
av2 = 0 #rad/s 



def acceleration():
    pass


#   ani = animation.FuncAnimation(fig=, func=, frames=, interval=)

plt.show()



