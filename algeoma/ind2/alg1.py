import numpy as np

A = np.array([[5,0,0,0,0],[1,5,0,0,0],[1,1,5,0,0],[1,1,1,5,0],[1,1,1,1,5]])
b = np.array([1,1,1,1,1])
x1 = 1/5
x2 = (1 - x1)/5
x3 = (1 - x1 - x2)/5
x4 = (1 - x1 - x2 - x3)/5
x5 = (1 - x1 - x2 - x3 - x4)/5
x = np.array([x1,x2,x3,x4,x5])

print(x)