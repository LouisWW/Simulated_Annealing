import numpy as np
import matplotlib.pyplot as plt
from function import *


data = np.load('list_total_E_linear_Trange_1-00001_Npar_11_lengthMC_10000_stepsize_002_Niter_100.npy')

plot_dist(data,1000)

data_sorted = np.sort(data)

print("Where do you draw the line?")
dividing_number = input()
data_low = data_sorted[data_sorted<dividing_number]
data_high = data_sorted[data_sorted>dividing_number]


# plt.boxplot(data_sorted[0:len(data)/6])
# plt.boxplot(data_sorted[len(data)/6:len(data)-1])
plt.boxplot(data_low)
plt.boxplot(data_high)
plt.ylabel("Total energy of system (a.u.)")
plt.show()



