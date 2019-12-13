#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:30:03 2019
This code was implemented by Louis Weyland & Robin van den Berg'''

"""
from function import *
from change_configuration import *
import time 
import os

# Repetition represents the number of simulations so 100 

repetition=100
energ_dist=[]

for i in range(0,repetition):

    # Universal paramters
    length_mc = 10000
    iterations = 100
    av_stepsize = 0.02
    number_of_particles = 10
    T_begin= 0.5
    T_end= 0.0000001
    T_schedule = "linear"
    current_T_index = 0

    # create list with different temp used 
    # you can use, linear, exponential, logarithmic
    list_T = distributed_T(T_schedule, T_begin, T_end, length_mc, iterations)
    
    # create particles
    list_particles=[Particle() for k in range(number_of_particles)]

    #create circle
    circle=Circle(r=1)

    # get the total energy of the system
    total_E=total_energy(list_particles)
    list_total_E = []
 
    # For each markov chain
    for j in range(0, length_mc):
        
        # if true --> update the temperature
        if j % iterations == 0:
            T = list_T[current_T_index]
           
            current_T_index += 1

        list_particles = change_config(list_particles, T, av_stepsize)
        list_total_E.append(total_energy(list_particles))
        
    #plot_circle(list_particles,circle)
    #print("Total energy",total_energy(list_particles))
        
    energ_dist.append(list_total_E[-1])
        


# save file under file name with loads of parameters in the name
filename_total_E_list = ("list_total_E_" + T_schedule + "_Trange_" + str(T_begin) +
                            "-" + str(T_end) + "_Npar_" + str(number_of_particles)
                            + "_lengthMC_" + str(length_mc) + "_stepsize_" + str(av_stepsize)
                            + "_Niter_" + str(iterations))


filename_total_E_list = filename_total_E_list.replace('.', '')

# to save the files uncommend the lines below
#directory=os.chdir("../Data/")
#np.save(filename_total_E_list, energ_dist)
#plot_dist(energ_dist,repetition,filename_total_E_list)

# =============================================================================
