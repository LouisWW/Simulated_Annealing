import numpy as np
import matplotlib.pyplot as plt 
import random 

# =============================================================================


# calculate the energy level of one particle
def calc_energy_1p(coordinates, particlenumber, list_particles):
    E = 0
    for i in range(len(list_particles)):
        distance = np.sqrt((coordinates[0] - list_particles[i].x) ** 2 + \
                           (coordinates[1] - list_particles[i].y) ** 2)
        if distance != 0:
            E += 1 / distance

    return E

# =============================================================================

# Class to create the different objects 

class particle:
    
    def __init__(self):
        self.x=random.uniform(-1,1)
        # To make sure that the points are within the circle
        self.y=random.uniform(-np.sqrt(1-self.x**2),np.sqrt(1-self.x**2))
     
     
class circle:
    
    def __init__(self):
        self.theta=np.linspace(0,2*np.pi,100)
        self.radius=1
        self.x=self.radius*np.cos(self.theta)
        self.y=self.radius*np.sin(self.theta)
   

# =============================================================================    

#  Plot the circle with the points in it 
    
def plot_circle(particles,circle):
    
    x,y = zip(*[((i.x),float(i.y)) for i in particles])

    plt.axis("equal")
    plt.scatter(x,y,color='k')
    plt.plot(circle.x,circle.y,'k')
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    plt.show()
    

# =============================================================================
