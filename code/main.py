'''This code was implemented by Louis Weyland & Robin van den Berg'''

from function import *
from change_configuration import *

length_mc = 100000
iterations = 100
list_T = np.linspace(0.1, 0.0000001, length_mc/iterations)
print(list_T)
av_stepsize = 0.02

# create particles
number_of_particles = 35

list_particles=[Particle() for i in range(number_of_particles)]

#create circle
circle=Circle(r=1)
plot_circle(list_particles,circle)
total_E=total_energy(list_particles)
list_total_E = []

current_T_index = 0
T = 0.1
print(len(list_T))
for i in range(0, length_mc):
    if i % iterations == 0:
        T = list_T[current_T_index]
        # print("i: ", i)
        # print("T: ", T)
        current_T_index += 1

    list_particles = change_config(list_particles, T, av_stepsize)
    list_total_E.append(total_energy(list_particles))

plot_circle(list_particles, circle)

plt.figure()
plt.plot(list_total_E)
plt.show()

