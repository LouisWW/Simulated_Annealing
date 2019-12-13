#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Wed Dec  4 15:30:03 2019
This code was implemented by Louis Weyland & Robin van den Berg'''


This file takes a list of particles representating one configuration and 
produces another one

TO_DO in future: USE FORCE OF ALL PARTICLES TO INFLUENCE CONFIGUREATION
"""
import numpy as np
from function import *
import global_variables


def change_config(list_particles, T, av_stepsize):
    N = len(list_particles)

    # av_stepsize = circle.r/100

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
            # if energy is lower, we accept the new state
            if dE < 0:
                list_particles[i].x = temp_x
                list_particles[i].y = temp_y


            # if energy is higher, but we still accept the value
            if (dE > 0) and (accept_config(dE, T) == True):
                list_particles[i].x = temp_x
                list_particles[i].y = temp_y

    return list_particles
