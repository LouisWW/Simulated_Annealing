from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def distributed_T(name_distribution, T_begin, T_end, length_mc, iterations):

    list_T = []
    if name_distribution == "linear":
        list_T = np.linspace(T_begin, T_end, length_mc / iterations)

    if name_distribution == "exponential":

        def func(x, T_begin, alpha):
            return T_begin*alpha**x

        x = [0, length_mc / iterations]
        yn = [T_begin, T_end]
        popt, pcov = curve_fit(func, x, yn)

        for i in range(length_mc/iterations):
            list_T.append(popt[0]*popt[1]**i)

        plt.figure()
        plt.plot(list_T)
        plt.show()

    if name_distribution == "logarithmic":

        def func(x, c, d):
            return c/np.log(x+d)

        x = [0, length_mc / iterations]
        yn = [T_begin, T_end]
        popt, pcov = curve_fit(func, x, yn)

        for i in range(length_mc/iterations):
            list_T.append(popt[0]/np.log(i+popt[1]))

        plt.figure()
        plt.plot(list_T)
        plt.show()


distributed_T("exponential", T_begin=0.1, T_end=0.0000001, length_mc=100000, iterations=100)
distributed_T("logarithmic", T_begin=0.1, T_end=0.0000001, length_mc=100000, iterations=100)




