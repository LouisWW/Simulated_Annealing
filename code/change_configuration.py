###This file takes a list of particles representating one configuration and produces another
###one

import numpy as np
import global_variables

### TO_DO: USE FORCE OF ALL PARTICLES TO INFLUENCE CONFIGUREATION

def change_config(list_particles, T):
    N = len(list_particles)


    # av_stepsize = circle.r/100
    av_stepsize = 0.02
    # r_squared = circle.r**2
    r_squared = 1 ** 2

    # change the location of every particle
    for i in range(N):

        # move particle i
        temp_x = list_particles[i].x + np.random.choice([-1, 1]) * np.random.exponential(1/av_stepsize)
        temp_y = list_particles[i].y + np.random.choice([-1, 1]) * np.random.exponential(1/av_stepsize)

        # check whether point falls within sphere
        if temp_y**2 + temp_x**2 <= r_squared:

            # compare the energy of the old configuration to the new one
            dE = calc_energy_1p([temp_x, temp_y], i, list_particles) - calc_energy_1p([temp_x, temp_y], i, list_particles)

            # if energy is lower, we accept the new state
            if dE < 0:
                list_particles.x = temp_x
                list_particles.y = temp_y

            # if energy is higher, but we still accept the value
            if dE > 0 and accept_config(dE, T) == True:
                list_particles.x = temp_x
                list_particles.y = temp_y

# calculate the energy level of one particle
def calc_energy_1p(coordinates, particlenumber, list_particles):
    E = 0
    for i in range(len(list_particles)):
        distance = np.sqrt((coordinates[0]-list_particles[i].x)**2+(coordinates[1]-list_particles[i].y)**2)
        if distance != 0:
            E += 1/distance

    return E