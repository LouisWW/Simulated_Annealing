#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:30:03 2019
This code was implemented by Louis Weyland & Robin van den Berg'''

"""
from function import *
from change_configuration import *
import time 


start_time = time.time()


repetition=30
energ_dist=[]

for i in range(0,repetition):

    length_mc = 10000
    iterations = 100
    av_stepsize = 0.02
    number_of_particles = 4
    T_begin=0.1
    T_end= 0.0000001
    current_T_index = 0

    list_T = np.linspace(T_begin, T_end, length_mc/iterations)

    # create particles
    list_particles=[Particle() for i in range(number_of_particles)]

    #create circle
    circle=Circle(r=1)

    total_E=total_energy(list_particles)
    list_total_E = []

    for i in range(0, length_mc):
        # update the temp
        if i % iterations == 0:
            T = list_T[current_T_index]
            current_T_index += 1

        list_particles = change_config(list_particles, T, av_stepsize)
        list_total_E.append(total_energy(list_particles))
        
    #plot_circle(list_particles,circle)
    print("Total energy",total_energy(list_particles))
        
    energ_dist.append(list_total_E[-1])
        
print("--- %s seconds ---" % (time.time() - start_time))

#%%

# =============================================================================

# plot figures 

plot_dist(energ_dist,repetition)  

# =============================================================================
  
        
    
    


