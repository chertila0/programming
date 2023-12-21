import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def sequence(n):
    return ((n**2) / (3*n + 1)) - (2*n**2 + 3) / (6*n - 1)

def plot_points(m):
    x = np.arange(1, m+1)
    y = sequence(x)
    n = Symbol("n")   
    a =limit(((n**2) / (3*n + 1)) - ((2*n**2 + 3) / (6*n - 1)), n, oo)
    print(a)
    # (k, 0) - blue colour
    plt.plot(x, np.zeros_like(x), 'bo', label='$(k, 0)$')

    # (0, x_k) - green color
    plt.plot(np.zeros_like(x), y, 'go', label='$(0, x_k)$')
    # (k, x_k) - red color
    plt.plot(x, y, 'ro', label='$(k, x_k)$')
    plt.plot(0, a, 'ro', color='orange')
    

    plt.xlabel('$k$')
    plt.ylabel('$x_k$')
    plt.legend()
    plt.grid()
    plt.show()

m = 30  # number of points
plot_points(m)
