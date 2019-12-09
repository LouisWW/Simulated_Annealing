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


repetition=20
energ_dist=[]

for i in range(0,repetition):

    length_mc = 10000
    iterations = 100
    av_stepsize = 0.2
    number_of_particles = 10
    T_begin= 1

    T_end= 0.0001
    current_T_index = 0

    # create list with different temp used # you can use, linear, exponential, logarithmic
    # logarithmic is very hard coded still because I couldnt get it to fit
    list_T = distributed_T("linear", T_begin, T_end, length_mc, iterations)
    
    # create particles
   
    list_particles=[Particle() for k in range(number_of_particles)]

    #create circle
    circle=Circle(r=1)

    total_E=total_energy(list_particles)
    list_total_E = []

    for j in range(0, length_mc):
        # update the temp
      
        
        if j % iterations == 0:
            T = list_T[current_T_index]
           
            current_T_index += 1

        list_particles = change_config(list_particles, T, av_stepsize)
        list_total_E.append(total_energy(list_particles))
        
    #plot_circle(list_particles,circle)
    #print("Total energy",total_energy(list_particles))
        
    energ_dist.append(list_total_E[-1])
        
print("--- %s seconds ---" % (time.time() - start_time))

#%%

# =============================================================================

# plot figures 

plot_dist(energ_dist,repetition)  
plot_whisker([energ_dist, energ_dist],"Markov Chain",["10","10"],'Test')
# =============================================================================
        
from scipy import stats

k2, p = stats.normaltest(energ_dist)

print(k2,p)





