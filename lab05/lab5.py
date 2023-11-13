import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.exp(-x*x) - x*x + 2*x
h = float(input())
h = round(1/h)
x = np.linspace(1,2,h)
y = []
for i in x:
    y.append(f(i))
plt.title('График') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.grid()
plt.plot(x, y)
plt.show()
