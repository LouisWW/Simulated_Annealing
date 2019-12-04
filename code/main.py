'''This code was implemented by Louis Weyland & Robin van den Berg'''

from function import *


# create particles
number_of_particles=5
list_particles=[Particle() for i in range(number_of_particles)]

#create circle
circle=Circle(r=1)

#Can also be deleted
for i in range(0,number_of_particles):
   print("x coordinates: ",list_particles[i].x,"Y coordinates :", list_particles[i].y)

#plot_circle(list_particles,circle)


total_energy=total_energy(list_particles)

# Can be deleted
print("total energy :",total_energy)


