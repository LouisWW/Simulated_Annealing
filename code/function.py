import numpy as np
import matplotlib.pyplot as plt 
import random
from scipy.optimize import curve_fit
from matplotlib.patches import Polygon


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
        
        
def plot_dist(energy_dist,repetition,name=None):
    plt.figure()
    ax = plt.gca()
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False)
    entries, bin_edges, patches = plt.hist(energy_dist, bins =int(repetition/4) , \
                                           normed=True,color='k')
    plt.title("The distribution of the average total energy", fontsize=12)
    plt.xlabel("Average total energy", fontsize=9, fontweight='bold')
    plt.ylabel("Occurrence (#)", fontsize=9, fontweight='bold')
    plt.show()
            
    if name !=None :
        plt.savefig(name,dpi=300)
    
    
def plot_whisker(energy_dist,xlabel,xunits,name=None):
    plt.figure()
    ax = plt.gca()
    ax.spines["top"].set_visible(False)  
    ax.spines["right"].set_visible(False)
    # Inspired from the matplotlib example 
    # https://matplotlib.org/3.1.1/gallery/statistics/boxplot_demo.html
    ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)
    ax.set_axisbelow(True)
    
    box_colors = ['darkkhaki', 'royalblue']
    num_boxes = len(energy_dist)
    medians = np.empty(num_boxes)    
    bp = ax.boxplot(energy_dist, notch=0, sym='+', vert=1, whis=1.5)
   
    for i in range(num_boxes):
        box = bp['boxes'][i]
        boxX = []
        boxY = []
        for j in range(5):
            boxX.append(box.get_xdata()[j])
            boxY.append(box.get_ydata()[j])
            box_coords = np.column_stack([boxX, boxY])
            # Alternate between Dark Khaki and Royal Blue
            ax.add_patch(Polygon(box_coords, facecolor=box_colors[i % 2]))
            # Now draw the median lines back over what we just filled in
            med = bp['medians'][i]
            medianX = []
            medianY = []
            for j in range(2):
                medianX.append(med.get_xdata()[j])
                medianY.append(med.get_ydata()[j])
                ax.plot(medianX, medianY, 'k')
                medians[i] = medianY[0]
                
      
    pos = np.arange(num_boxes) + 1
    upper_labels = [str(np.round(s, 2)) for s in medians]
    weights = ['bold', 'semibold']
    for tick, label in zip(range(num_boxes), ax.get_xticklabels()):
        k = tick % 2
        ax.text(pos[tick], .97, upper_labels[tick],
                 transform=ax.get_xaxis_transform(),
                 horizontalalignment='center', size=9,
                 weight=weights[k], color=box_colors[k])
        


    plt.boxplot(energy_dist)
    ax.set_xticklabels(xunits)
    plt.title("The distribution of the average total energy", fontsize=12)
    plt.xlabel(xlabel, fontsize=9, fontweight='bold')
    plt.ylabel("Average total energy", fontsize=9, fontweight='bold')
  
 

            
    if name !=None :
        plt.savefig(name,dpi=300)
        
    plt.show()
        

    
    
    

# =============================================================================
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

