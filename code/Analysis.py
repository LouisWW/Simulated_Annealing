#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:30:03 2019
This code was implemented by Louis Weyland & Robin van den Berg'''

N.B. This script can't run without the files
"""

import os
import matplotlib.pyplot as plt 
from function import *


#load a file 
repetition=100
# plot figures 


###############################################################################
#%%
# Check the different step sizes


directory=os.chdir("../Data/")
step_1=np.load("list_total_E_linear_Trange_05-1e-07_Npar_10_lengthMC_10000_stepsize_1_Niter_100.npy")
step_02=np.load("list_total_E_linear_Trange_05-1e-07_Npar_10_lengthMC_10000_stepsize_002_Niter_100.npy")
step_005=np.load("list_total_E_linear_Trange_05-1e-07_Npar_10_lengthMC_10000_stepsize_0005_Niter_100.npy")


plot_dist(step_1,repetition,'list_total_E_linear_Trange_05-1e-07_Npar_10_lengthMC_10000_stepsize_1_Niter_100')
plot_dist(step_02,repetition,'list_total_E_linear_Trange_05-1e-07_Npar_10_lengthMC_10000_stepsize_002_Niter_100')
plot_dist(step_005,repetition,'list_total_E_linear_Trange_05-1e-07_Npar_10_lengthMC_10000_stepsize_0005_Niter_100')


# Divide the peaks in lower and higher energy
lower_step_02=[]
higher_step_02=[]
lower_step_005=[]
higher_step_005=[]



for i in step_02:
    
    # define the threshold   38.92 = local minimum so lower correspond to the 
    # global minimum with the correct configuration
    if i<38.92:
        lower_step_02.append(i)
    else:
        higher_step_02.append(i)

    

for i in step_005:
    # define the threshold
    if i<38.75:
        lower_step_005.append(i)
    elif i>38.92 and i<40:
        higher_step_005.append(i)




 
# Print the variance and the mean values of the different means              
directory=os.chdir("../Data/")   
print("Variance of step 1 : ",np.var(step_1), " | mean :",np.mean(step_1))
print("Variance of higher_step 02 : ",np.var(higher_step_02)," | mean :",np.mean(higher_step_02))
print("Variance of lower_step 02 : ",np.var(lower_step_02)," | mean :",np.mean(lower_step_02))
print("Variance of higher_step 005 : ",np.var(higher_step_005)," | mean :",np.mean(higher_step_005))
print("Variance of lower_step 005 : ",np.var(lower_step_005)," | mean :",np.mean(lower_step_005))

    


###############################################################################
#%%
# Check the different repetition of the Markov chain

Markov_1000=np.load("list_total_E_linear_Trange_05-1e-07_Npar_10_lengthMC_1000_stepsize_002_Niter_100.npy")
Markov_100000=np.load("list_total_E_linear_Trange_05-1e-07_Npar_10_lengthMC_100000_stepsize_002_Niter_100.npy")

plot_dist(Markov_1000,repetition,'list_total_E_linear_Trange_05-1e-07_Npar_10_lengthMC_1000_stepsize_002_Niter_100')
plot_dist(Markov_100000,repetition,'list_total_E_linear_Trange_05-1e-07_Npar_10_lengthMC_100000_stepsize_002_Niter_100')

# Divide in higher and lower energy
lower_Markov_1000=[]
higher_Markov_1000=[]
lower_Markov_100000=[]
higher_Markov_100000=[]

for i in Markov_1000:
    
    if i<38.92:
        lower_Markov_1000.append(i)
    elif i>38.92 and i<40:
        higher_Markov_1000.append(i)


for i in Markov_100000:
    
    if i<38.92:
        lower_Markov_100000.append(i)
    elif i>38.92 and i<40:
        higher_Markov_100000.append(i)


    
print("Variance of higher_Markov_1000 =",np.var(higher_Markov_1000)," | mean :",np.mean(higher_Markov_1000))
print("Variance of low_Markov_1000 =",np.var(lower_Markov_1000),"  | mean :",np.mean(lower_Markov_1000))

print("Variance of higher_Markov_100000 =",np.var(higher_Markov_100000)," | mean :",np.mean(higher_Markov_100000))
print("Variance of low_Markov_100000 =",np.var(lower_Markov_100000),"  | mean :",np.mean(lower_Markov_100000))

     
        

###############################################################################
#%%

# Plot the theorectical values


in_middle = [total_eng_theory(i, False) for i in range(2,18)]
on_rim = [total_eng_theory(i, True) for i in range(2,18)]
num_particles = [i for i in range(2,18)]
plt.xlabel("Number of particles (#)", fontweight='bold',fontsize=12)
plt.ylabel("System energy (a.u.)", fontweight='bold',fontsize=12)
plt.plot(num_particles, in_middle, 'k-',linewidth=1)
plt.plot(num_particles, on_rim, 'r--',linewidth=1)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim([2, 17])
plt.ylim([min(in_middle[0],on_rim[0]), max(in_middle[-1], on_rim[-1])])
plt.legend(["one in middle", "all on the rim"])
#plt.savefig("Theor_eng",dpi=300)

###############################################################################
#%%


print("11 and 12 particle ")

par_11=np.load("list_total_E_linear_Trange_05-1e-07_Npar_11_lengthMC_10000_stepsize_002_Niter_100.npy")
par_12=np.load("list_total_E_linear_Trange_05-1e-07_Npar_12_lengthMC_10000_stepsize_002_Niter_100.npy")

plot_dist(par_11,100)
plot_dist(par_12,100)

lower_par_11=[]
higher_par_11=[]

lower_par_12=[]
higher_par_12=[]

for i in par_11:
    if i <48.62:
        lower_par_11.append(i)
    else:
        higher_par_12.appned(i)

for i in par_11:
    if i <48.62:
        lower_par_11.append(i)
    else:
        higher_par_12.appned(i)

###############################################################################

