import matplotlib.pyplot as plt
import numpy as np
from sympy import *


def pic1():
    x = [round(i, 2) for i in np.arange(-20, 21, 0.1)]
    y = [round((i/(i-2)),2) for i in x]
    plt.plot(x, y, linewidth=2, color='red')
    plt.title('График функции x/(x-2)', fontsize=15)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14) 
    plt.grid(True)
def pic2():
    x = np.arange(-100,100,0.1)
    y = np.arcsin(2/(x+3))
    plt.plot(x, y, linewidth=2, color='blue')
    plt.title('График функции arcsin(2/(x+3))', fontsize=15)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14) 
    plt.grid(True)

plt.figure()
pic1()
plt.figure()
pic2()
plt.show()