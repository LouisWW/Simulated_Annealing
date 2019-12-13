# this file defines the function that will initialise the global variables

from function import *

def init_global(length_MC, n_particles):

    global list_acceptance
    list_acceptance = np.zeros(length_MC*n_particles)

    global counter
    counter = 0