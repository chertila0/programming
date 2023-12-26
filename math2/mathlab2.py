import matplotlib.pyplot as plt 
import numpy as np


def f(x):
    return x * np.sin(x)

def kasat(x):
    return -np.pi*(x-np.pi)

def normal(x):
    return 1/np.pi*(x-np.pi)

x = np.linspace(-7,7,70)
y = f(x)

plt.plot(x,y, label = 'f(x)')
plt.plot(x,kasat(x), label = 'Касательная')
plt.plot(x,normal(x), label = 'Нормальная прямая')
plt.plot(np.pi, f(np.pi), 'ro', label = 'Точка касания')
plt.gca().set_aspect('equal')
plt.legend()
plt.grid()
plt.show()
