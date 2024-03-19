import numpy as np
from numpy.linalg import matrix_power

A = np.array([[-1,2,-4], [1,-1,7], [-1,0,0]])
B = np.array([[1,0,0],[0,2,0],[1,0,3]])
C = np.array([[3,8,-1],[0,8,0],[2,-1,3]])
D = (np.dot(matrix_power(A,2), B) + np.dot(matrix_power(B,3),A)).T
F = np.dot(B,C)
X = np.dot(np.linalg.inv(D),F)
print('X =', X)
print('Проверка')
print('BC=', F)
print('Конечный результат должен быть равен ВС')
print(np.dot(D,X))