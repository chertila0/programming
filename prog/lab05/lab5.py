import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.exp(-x*x) - x*x + 2*x

def f_pr(x):
    return (-x*x - 1)*math.exp(-x*x) - 2*x + 2
h = float(input())
h = round(1/h)
tochka_kas = 1.4
x = np.linspace(1,2,h)
y = []
for i in x:
    y.append(f(i))
x1 = [1.0, 2.0]
y1 =[]
for i in x1:
    y1.append(f(tochka_kas) + f_pr(tochka_kas) * (i - tochka_kas))
plt.title('График') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.grid()
plt.plot(x, y)
plt.plot(x1, y1)
plt.plot(tochka_kas, f(tochka_kas), "ro")
plt.show()
