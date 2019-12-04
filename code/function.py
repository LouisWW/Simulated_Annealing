import numpy as np
import matplotlib.pyplot as plt 
import random
from numba import jit, void, int_, double

# =============================================================================

# calculate the energy level of one particle

def calc_energy_1p(coordinates, particle_number, list_particles):
    E = 0
    for i in range(len(list_particles)):
        
        if i != particle_number:
            distance = np.sqrt((coordinates[0] - list_particles[i].x) ** 2 + \
                           (coordinates[1] - list_particles[i].y) ** 2)

            E += 1 / distance

    return E




def total_energy(list_particles):
    
    total_E=0
    
    for i in range(0,len(list_particles)):
        
        for k in range(i+1,len(list_particles)):
            
            distance= np.sqrt((list_particles[i].x - list_particles[k].x) ** 2 + \
                           (list_particles[i].y - list_particles[k].y) ** 2)
          
           
            total_E+=1/distance
            
    
    return total_E
            
            
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
    
def plot_energy(list_total_energy,name=None):
    plt.figure()
    ax = plt.gca()
    #ax.set_facecolor('lightgray')
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False)
    plt.plot(list_total_energy,color='k')
    plt.xlabel('CMTC',fontweight='bold',fontsize=12)
    plt.ylabel('# of Steps',fontweight='bold',fontsize=12)
    plt.xlim(0,len(list_total_energy))
    plt.xticks(fontsize=9)
    plt.yticks(fontsize=9)
    
    if name !=None :
        plt.savefig(name,dpi=300)
        
        
def plot_dist(energ_dist,repetition,name=None):
    plt.figure()
    ax = plt.gca()
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False)
    entries, bin_edges, patches = plt.hist(energ_dist, bins =int(repetition/4) , \
                                           normed=True,color='k')
    plt.title("The distribution of the average total energy", fontsize=12)
    plt.xlabel("Average total energy", fontsize=9, fontweight='bold')
    plt.ylabel("Occurrence (#)", fontsize=9, fontweight='bold')
            
    if name !=None :
        plt.savefig(name,dpi=300)
    
    

# =============================================================================
