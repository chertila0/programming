import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy import Symbol,limit
from math import pi,log


#1
def pic1():
    x = [round(i, 2) for i in np.arange(-20, 21, 0.1)]
    y = [round((i/(i-2)),2) for i in x]
    plt.plot(x, y, linewidth=2, color='red')
    plt.title('График функции x/(x-2)', fontsize=15)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14) 
    plt.grid(True)
def pic2():
    x = np.linspace(-15,11,1000)
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

#2
# x1 = np.linspace(-np.pi/2 + 0.01, np.pi/2 - 0.01, 1000)
# y1 = x1 * np.tan(x1) / (np.pi - x1)
# x2 = np.linspace(np.pi/2 + 0.01, np.pi - 0.01, 1000)
# y2 = x2 * np.tan(x2) / (np.pi - x2)
# x3 = np.linspace(np.pi + 0.01, 3*np.pi/2 - 0.01)
# y3 = x3 * np.tan(x3) / (np.pi - x3)
# x4 = np.linspace(3*np.pi/2 + 0.01, 2*np.pi - 0.01)
# y4 = x4 * np.tan(x4) / (np.pi - x4)

# n = Symbol('n') 
# a = limit(n * sp.tan(n) / (sp.pi - n), n, sp.pi)
# print(a)

# plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, color='red')
# plt.plot(pi,a,'o', color='orange')
# plt.grid(True)
# plt.show()

# #3
# x1 = np.linspace(-10,0.99999, 1000)
# y1 = np.log(1 - x1)
# x2 = np.linspace(1, 10, 1000)
# y2 = [i*i - i for i in x2]
# n = Symbol('n')
# lp = limit(sp.log(1 - n), n, 1, dir='-')
# rp = limit(n*n - n, n, 1, dir='+')
# print(f" Предел функции слева {lp}, справа {rp}")
# plt.plot(x1,y1,x2,y2, color='red')
# plt.plot(1,1,'ro', color='orange')
# plt.text(-2.5,10, 'Точка разрыва')
# plt.grid(True)
# plt.show()







