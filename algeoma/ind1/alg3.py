import numpy as np
from numpy.linalg import matrix_power

A = np.array([[2,-1,-1],[0,2,-1],[0,0,-1]])
B = np.array([[-1,0,0],[1,-3,0],[1,1,-5]])
C = (matrix_power(A,3) - 2*matrix_power(A,2) + 3*A).T
D = 4*matrix_power(B,2)-B
X = np.dot(np.linalg.inv(C), D)
print(X)
print('4B**2 - B =', D)
print(np.dot(C,X))