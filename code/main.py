'''This code was implemented by Louis Weyland & Robin van den Berg'''

from function import *
from change_configuration import *
import time 


start_time = time.time()

length_mc = 1000
iterations = 100
av_stepsize = 0.02
number_of_particles = 30
T_begin=0.1
T_end= 0.0000001
current_T_index = 0

# create list with different temp used
list_T = np.linspace(T_begin, T_end, length_mc/iterations)

# create particles
list_particles=[Particle() for i in range(number_of_particles)]

#create circle
circle=Circle(r=1)
plot_circle(list_particles,circle,'Init')


total_E=total_energy(list_particles)
list_total_E = []

for i in range(0, length_mc):
    # update the temp
    if i % iterations == 0:
        T = list_T[current_T_index]
        current_T_index += 1

    list_particles = change_config(list_particles, T, av_stepsize)
    list_total_E.append(total_energy(list_particles))
    
print("--- %s seconds ---" % (time.time() - start_time))

# =============================================================================

# plot figures 

plot_circle(list_particles, circle,'Final')
plot_energy(list_total_E,'Total_energy')
plt.show()

# =============================================================================

