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



start_time = time.time()


repetition=100
energ_dist=[]

for i in range(0,repetition):

    length_mc = 10000
    iterations = 100
    av_stepsize = 0.005
    number_of_particles = 10
    T_begin= 1
    T_end= 0.0001
    T_schedule = "linear"
    current_T_index = 0

    # create list with different temp used # you can use, linear, exponential, logarithmic
    # logarithmic is very hard coded still because I couldnt get it to fit
    list_T = distributed_T(T_schedule, T_begin, T_end, length_mc, iterations)
    
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


# save file under file name with loads of parameters in the name
filename_total_E_list = ("list_total_E_" + T_schedule + "_Trange_" + str(T_begin) +
                            "-" + str(T_end) + "_Npar_" + str(number_of_particles)
                            + "_lengthMC_" + str(length_mc) + "_stepsize_" + str(av_stepsize)
                            + "_Niter_" + str(iterations))

filename_total_E_list = filename_total_E_list.replace('.', '')

directory=os.chdir("../Data/")
np.save(filename_total_E_list, list_total_E)
plot_dist(energ_dist,repetition,filename_total_E_list)

# =============================================================================
#%%
# plot figures 

plot_dist(energ_dist,repetition)  
plot_circle(list_particles,circle)
# =============================================================================

plt.boxplot(energ_dist)
        
from scipy import stats

k2, p = stats.normaltest(energ_dist)

print(k2,p)





