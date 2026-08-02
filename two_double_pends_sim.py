import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# constants / parameters
g = 9.81 #m/s^2[down]
m1 = 1 #kg
m2 = 1 #kg
l1 = 1 #m
l2 = 1 #m
dt = 0.02 #delta time, the time between each step/drawing of the visualisation
t_max = 15 # maximum time for the simulation to run for

n_steps=int(t_max/dt) # number of frames per simulation

# starting conditions for pend A
theta1_A = 3*np.pi/5 #degrees # np.pi is numpy's approximation of pi
theta2_A = np.pi/4 #degrees
av1_A = 0 #av= angular vecocity of each mass in rad/s angular velocity is the change in angular displacement over the change in time
av2_A = 0 #rad/s 

#starting conditions for pend B
theta1_B = theta1_A+0.01
theta2_B = theta2_A+0.01
av1_B = 0
av2_B = 0


def accelerations(theta1,theta2,av1,av2):
    delta = theta1-theta2
    denom = (m2*(l1**2)*(l2**2))*((m1+m2)-m2*(np.cos(delta)**2))
    

    alpha1 = (
        (m2*l1*(l2**2))*(-m2*l2*(av2**2)*(np.sin(delta))-(m1+m2)*g*(np.sin(theta1))-m2*l1*(av1**2)*(np.sin(delta))*(np.cos(delta))+m2*g*(np.sin(theta2))*(np.cos(delta))) / denom
    )

    alpha2 = (
        (m2*(l1**2)*l2)*((m1+m2)*l1*(av1**2)*(np.sin(delta))-(m1+m2)*g*(np.sin(theta2))+m2*l2*(av2**2)*(np.cos(delta))*(np.sin(delta))+(m1+m2)*g*(np.cos(delta))*(np.sin(theta1))) / denom
    )

    return alpha1, alpha2

def step(theta1,theta2,av1,av2,dt): #euler integration!! -will use RK4 in future :)
    alpha1, alpha2 = accelerations(theta1,theta2,av1,av2)

    theta1_new = theta1 + av1*dt
    theta2_new = theta2 + av2*dt
    av1_new = av1 + alpha1*dt
    av2_new = av2 + alpha2*dt

    return theta1_new, theta2_new, av1_new, av2_new

#arrays to hold data for pendulums
theta1_A_history=np.zeros(n_steps) #pend A
theta2_A_history=np.zeros(n_steps) #creates an empty array the size of the number of frames, will store each angle as the sim goes through each step

theta1_B_history=np.zeros(n_steps)  #pend B
theta2_B_history=np.zeros(n_steps)

for i in range(n_steps): # updating values every frame.
    #pend A
    theta1_A_history[i] = theta1_A #stores angle in coordsponding frame in the array
    theta2_A_history[i] = theta2_A
    theta1_A, theta2_A, av1_A, av2_A = step(theta1_A,theta2_A,av1_A,av2_A,dt) #updates values each step/frame

    #pend B
    theta1_B_history[i] = theta1_B
    theta2_B_history[i] = theta2_B
    theta1_B, theta2_B, av1_B, av2_B = step(theta1_B,theta2_B,av1_B,av2_B,dt)

#convert angles in positions (x1,y1) (x2,y2) for pend B
x1_A = l1*(np.sin(theta1_A_history))
y1_A = -l1*(np.cos(theta1_A_history))

x2_A = l1*(np.sin(theta1_A_history)) + l2*(np.sin(theta2_A_history))
y2_A = -l1*(np.cos(theta1_A_history)) - l2*(np.cos(theta2_A_history))

#positions for pend B
x1_B = l1*(np.sin(theta1_B_history))
y1_B = -l1*(np.cos(theta1_B_history))

x2_B = l1*(np.sin(theta1_B_history)) + l2*(np.sin(theta2_B_history))
y2_B = -l1*(np.cos(theta1_B_history)) - l2*(np.cos(theta2_B_history))


#setting up visuals
fig, ax = plt.subplots(figsize=(8,8)) 
ax.set_xlim(-(l1 + l2 + 1),l1 + l2 + 1) #domain is 1 unit greater the max arms length on either side
ax.set_ylim(-(l1 + l2 + 1),l1 + l2 + 1)
ax.set_aspect('equal')

line_A, = ax.plot([],[], "o-", color='red') # x y as arrrays so i can animate through them with my theta1_history for pend A
trail_A, = ax.plot([],[],'-', color='red')

line_B, = ax.plot([],[], "o-", color='blue') # pend B
trail_B, = ax.plot([],[],'-', color='blue')

def init(): #starting state for animation
    line_A.set_data([],[])
    trail_A.set_data([],[])

    line_B.set_data([],[])
    trail_B.set_data([],[])
    return line_A, trail_A, line_B, trail_B

def animate(i):
    line_A.set_data([0,x1_A[i],x2_A[i]], [0,y1_A[i],y2_A[i]]) #draws the line from origin to mass one to mass two updates as i increases because i is frame number
    start=max(0, i-200)
    trail_A.set_data(x2_A[start:i], y2_A[start:i])

    line_B.set_data([0,x1_B[i],x2_B[i]], [0,y1_B[i],y2_B[i]]) #draws the line from origin to mass one to mass two updates as i increases because i is frame number
    start=max(0, i-200)
    trail_B.set_data(x2_B[start:i], y2_B[start:i])
    return line_A, trail_A, line_B, trail_B

ani = animation.FuncAnimation(fig, animate, frames=n_steps, init_func=init, interval=dt*1000, blit=True)
plt.show()