 Minimising The Energy of Charged Particle Configurations on a Circular Surface by Means of Simulated Annealing
---------

Finding the minimum energy configuration for multiple electrons confined to a 
circle can't be solved analytically. Numerical methods such the Simulated Annealing allow through their heuristic approach to find an optimum minimum energy configuration.
The main.py, random electron are generated in a circle. length_mc is the length of the Makrov chain 
, iteration defines the number of Markov states confined to a certain temperature level.
The temperature corresponds to the cooling scheme of the Simulated Annealing. One can choose between linear, exponential,
logarithmic and sigmoidal cooling schedule. The file dist_of_total_energy.py has the same function as the main.py but repeat the calculation in order to get a distribution of the obtained minimum energy
configuration. The file Analysis plots the results. This file is hardcoded and loads the filename based on the parameter
used in the previous file.
The attached report contains all the background information and the results obtained using the
given algorithms.
