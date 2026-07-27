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



def accelerations(theta1,theta2,av1,av2):
    delta=theta1-theta2
    denom=(m2*(l1**2)*(l2**2))*((m1+m2)-m2*(np.cos(delta)**2))
    

    alpha1 = (
        (m2*l1*(l2**2))*(-m2*l2*(av2**2)*(np.sin(delta))-(m1+m2)*g*(np.sin(theta1))-m2*l1*(av1**2)*(np.sin(delta))*(np.cos(delta))+m2*g*(np.sin(theta2))*(np.cos(delta))) / denom
    )

    alpha2 = (
        (m2*(l1**2)*l2)*((m1+m2)*l1*(av1**2)*(np.sin(delta))-(m1+m2)*g*(np.sin(theta2))+m2*l2*(av2**2)*(np.cos(delta))*(np.sin(delta))+(m1+m2)*g*(np.cos(delta))*(np.sin(theta1))) / denom
    )

    return alpha1, alpha2

def step(theta1,theta2,av1,av2,dt): #euler integration!! -will use RK4 in future :)
    alpha1, alpha2 = accelerations(theta1,theta2,av1,av2)

    theta1_new=theta1 + av1*dt
    theta2_new=theta2 + av2*dt
    av1_new=av1 + alpha1*dt
    av2_new=av2 +alpha2*dt

    return theta1_new, theta2_new, av1_new, av2_new

theta1_history=np.zeros(n_steps) #creates an empty array the size of the number of frames, will store each angle as the sim goes through each step
theta2_history=np.zeros(n_steps)

for i in range(n_steps): # updating values every frame.
    theta1_history[i] = theta1 #stores angle in coordsponding frame in the array
    theta2_history[i] = theta2
    theta1, theta2, av1, av2 = step(theta1,theta2,av1,av2,dt) #updates values each step/frame

#convert angles in positions (x1,y1) (x2,y2)
x1 = l1*(np.sin(theta1))
y1 = -l1*(np.cos(theta1))

x2 = l1*(np.sin(theta1))+l2*(np.sin(theta2))
y2 = -l1*(np.cos(theta1))-l2*(np.cos(theta2))

#setting up visuals

fig, ax = plt.subplots(figsize=(8,8)) 
ax.set_xlim(-(l1+l2+1),l1+l2+1) #domain is 1 unit greater the max arms length on either side
ax.set_ylim(-(l1+l2+1),l1+l2+1)
ax.set_aspect('equal')

plt.show()


