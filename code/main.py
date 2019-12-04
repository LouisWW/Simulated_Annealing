'''This code was implemented by Louis Weyland & Robin van den Berg'''

from function import *


# create particles
number_of_particles=30
particles=[Particle() for i in range(number_of_particles)]

#create circle
circle=Circle(r=1)

for i in range(0,number_of_particles):
   print("x coordinates: ",particles[i].x,"Y coordinates :", particles[i].y)

plot_circle(particles,circle)



