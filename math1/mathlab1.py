import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol,tanh,pi,limit


#1
# def pic1():
#     x = [round(i, 2) for i in np.arange(-20, 21, 0.1)]
#     y = [round((i/(i-2)),2) for i in x]
#     plt.plot(x, y, linewidth=2, color='red')
#     plt.title('График функции x/(x-2)', fontsize=15)
#     plt.xlabel('x', fontsize=14)
#     plt.ylabel('y', fontsize=14) 
#     plt.grid(True)
# def pic2():
#     x = np.linspace(-15,11,1000)
#     y = np.arcsin(2/(x+3))
#     plt.plot(x, y, linewidth=2, color='blue')
#     plt.title('График функции arcsin(2/(x+3))', fontsize=15)
#     plt.xlabel('x', fontsize=14)
#     plt.ylabel('y', fontsize=14) 
#     plt.grid(True)

# plt.figure()
# pic1()
# plt.figure()
# pic2()
# plt.show()

#2
def pic():
    x = np.linspace(-5*np.pi, 5*np.pi, 1000)
    y = x * np.tan(x) / (np.pi - x)
    n = Symbol('n')
    x1 = limit(n * tanh(n) / (pi - n), n, pi)
    print(x1)
    
    plt.plot(x1)
    plt.grid(True)
    plt.show()

pic()






