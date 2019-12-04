###This file takes a list of particles representating one configuration and produces another
###one

import numpy as np
from function import *
import global_variables

### TO_DO: USE FORCE OF ALL PARTICLES TO INFLUENCE CONFIGUREATION

def change_config(list_particles, T):
    N = len(list_particles)

    # av_stepsize = circle.r/100
    av_stepsize = 0.2
    # r_squared = circle.r**2
    r_squared = 1 ** 2

    # change the location of every particle
    for i in range(N):

        # move particle i
        temp_x = list_particles[i].x + np.random.choice([-1, 1]) * np.random.exponential(av_stepsize)
        temp_y = list_particles[i].y + np.random.choice([-1, 1]) * np.random.exponential(av_stepsize)

        # check whether point falls within sphere
        if temp_y**2 + temp_x**2 <= r_squared:

            # compare the energy of the old configuration to the new one
            dE = calc_energy_1p([temp_x, temp_y], i, list_particles) - calc_energy_1p([list_particles[i].x, list_particles[i].y], i, list_particles)
            print("The energy change: ", dE)
            # if energy is lower, we accept the new state
            if dE < 0:
                print("energy is lower, lets move")
                list_particles[i].x = temp_x
                list_particles[i].y = temp_y

            # if energy is higher, but we still accept the value
            if (dE > 0) and (accept_config(dE, T) == True):
                print("we moved the particle because of chance")
                list_particles[i].x = temp_x
                list_particles[i].y = temp_y

    return list_particles


# mock function to test the change config function
def accept_config(dE, T):
    p_boltzmann = np.exp(-dE/T)
    print(p_boltzmann)
    if np.random.rand() > p_boltzmann:
        return False
    else:
        return True

list_particles = []
for i in range(3):
    list_particles.append(Particle())

circle=Circle(r=1)
plot_circle(list_particles,circle)

list_particles = change_config(list_particles, 100)

plot_circle(list_particles, circle)

