#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Dec  4 15:30:03 2019
This code was implemented by Louis Weyland & Robin van den Berg'''

"""
import numpy as np
import matplotlib.pyplot as plt 
import random
from scipy.optimize import curve_fit
from matplotlib.patches import Polygon


# =============================================================================

# calculate the energy level of one particle with respect to all the others 
# using the distance as parameter

def calc_energy_1p(coordinates, particle_number, list_particles):
    E = 0
    for i in range(len(list_particles)):
        
        if i != particle_number:
            distance = np.sqrt((coordinates[0] - list_particles[i].x) ** 2 + \
                           (coordinates[1] - list_particles[i].y) ** 2)

            E += 1 / distance

    return E



# calculate the total energy in  the system using the distance
    
def total_energy(list_particles):
    
    total_E=0
    
    for i in range(0,len(list_particles)):
        
        for k in range(i+1,len(list_particles)):
            
            distance= np.sqrt((list_particles[i].x - list_particles[k].x) ** 2\
                        + (list_particles[i].y - list_particles[k].y) ** 2)
          
           
            total_E+=1/distance
            
    
    return total_E


# calculate the theorectical energy for all the particles on the rim or 
# with one particle in the centre
    
def total_eng_theory(n_particles,on_rim=True):
    
            
    if on_rim==True:
        S_n=0
        for k in range(1,n_particles):
            S_n+=1/(np.sin(k*np.pi/n_particles))
        

        total_energy=(n_particles/4) * S_n
        
    if on_rim==False:
        S_n=0
        for k in range(1,n_particles-1):
            S_n+=1/(np.sin(k*np.pi/(n_particles-1)))
        
        total_energy=(n_particles-1)+((n_particles-1)/4) * S_n
            
    return total_energy
# =============================================================================

# Boltzmann equation

def accept_config(dE, T):
    p_boltzmann = np.exp(-dE/T)
    # print("dE", dE)
    # print("Boltzmann", p_boltzmann)
    if np.random.rand() > p_boltzmann:
        return False
    else:
        return True


# =============================================================================
        
    

# Class to create the different objects
class Particle:
    def __init__(self):
        self.x=random.uniform(-1,1)
        # To make sure that the points are within the circle
        self.y=random.uniform(-np.sqrt(1-self.x**2),np.sqrt(1-self.x**2))
     

class Circle:
    def __init__(self, r):
        self.theta=np.linspace(0,2*np.pi,100)
        self.radius=r
        self.x=self.radius*np.cos(self.theta)
        self.y=self.radius*np.sin(self.theta)
   

# =============================================================================    
        
        


#  Plot the circle with the points in it 
    
def plot_circle(list_particles,circle,name=None):
    
    x,y = zip(*[((i.x),float(i.y)) for i in list_particles])


    plt.figure()
   
    plt.scatter(x,y,color='k', s=25)
    plt.plot(circle.x,circle.y,'k')
    plt.xlabel("a.u.",fontweight='bold',fontsize=20)
    plt.ylabel("a.u.",fontweight='bold',fontsize=20)
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    plt.axis('off')
    plt.axis("equal")
    
    if name !=None :
        plt.savefig(name,dpi=300)

    plt.show()
    
# Plot the energy after each Markov state
    
def plot_energy(list_total_energy,name=None):
    plt.figure()
    ax = plt.gca()
    #ax.set_facecolor('lightgray')
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False)
    plt.plot(list_total_energy,color='k')
    plt.xlabel('CMTC',fontweight='bold',fontsize=12)
    plt.ylabel('System energy (a.u.)',fontweight='bold',fontsize=12)
    plt.xlim(0,len(list_total_energy))
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    if name !=None :
        plt.savefig(name,dpi=300)
        
    plt.show()
        

#  Plot the distribution of the  minimum energy achieved after each run      
   
def plot_dist(energy_dist,repetition,name=None):
    plt.figure()
    ax = plt.gca()
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False)
    entries, bin_edges, patches = plt.hist(energy_dist, bins =int(repetition/2) , \
                                           color='k')
    plt.xlabel("System energy (a.u.)", fontsize=12, fontweight='bold')
    plt.ylabel("Occurrence (#)", fontsize=12, fontweight='bold')

            
    if name !=None :
        plt.savefig(name,dpi=300)
        
    plt.show()
    

# Plot whisker plot (not used for the report)
    
def plot_whisker(energy_dist,xlabel,xunits,name=None):                
    plt.figure()
    ax = plt.gca()
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False)
    ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)
    ax.set_axisbelow(True)
    plt.boxplot(energy_dist[0])
    print(energy_dist[0])
    plt.boxplot([energy_dist[0],energy_dist[1]])
    plt.boxplot([energy_dist[0],energy_dist[2]])
    plt.boxplot([energy_dist[0],energy_dist[2],energy_dist[4]])
    plt.boxplot([energy_dist[0],energy_dist[2],energy_dist[3]])
    ax.set_xticklabels(xunits)

    ax.set_xticklabels(xunits)
    plt.xlabel(xlabel, fontsize=9, fontweight='bold')
    plt.ylabel("System energy (a.u.)", fontsize=9, fontweight='bold')
  
 

            
    if name !=None :
        plt.savefig(name,dpi=300)
        
    plt.show()
        

    
    
    

# =============================================================================

# function which determines the different cooling schedules such as linear,
# exponential or logarithmic and sigmoid. 
# T lenght is defined by the sum of the total Markov chain



def distributed_T(name_distribution, T_begin, T_end, length_mc, iterations):

    list_T = []
    if name_distribution == "linear":
        list_T = np.linspace(T_begin, T_end, length_mc / iterations)
        return list_T

    if name_distribution == "exponential":

        def func(x, T_begin, alpha):
            return T_begin*alpha**x

        x = [0, length_mc / iterations]
        yn = [T_begin, T_end]
        popt, pcov = curve_fit(func, x, yn)

        for i in range(length_mc/iterations):
            list_T.append(popt[0]*popt[1]**i)

        return list_T
        # plt.figure()
        # plt.plot(list_T)
        # plt.show()

    if name_distribution == "logarithmic":

        def func(t, a, b):
            return a + b * np.log(t)

        x = [0, length_mc / iterations]
        yn = [T_begin, T_end]
        #popt, pcov = curve_fit(func, x, yn, maxfev=10000)

        for i in range(length_mc/iterations):
            list_T.append(0.07/ np.log(i+1))

        return list_T
        # plt.figure()
        # plt.plot(list_T)
        # plt.show()
        
        
    if name_distribution == "sigmoid":
        
        def func(t):
            return 1/(1+np.e**t)

        x = [0, length_mc / iterations]
        yn = [T_begin, T_end]
        #popt, pcov = curve_fit(func, x, yn, maxfev=10000)

        for i in range(length_mc/iterations):
            list_T.append(0.07/ np.log(i+1))

        return list_T

