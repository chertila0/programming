import numpy as np

A = np.array([[4,-1,7],[0,1,-2],[0,0,9]])
B = np.array([[-1,1,0],[0,0,3],[6,2,-1]])
C = np.array([[5,1,1],[1,5,1],[1,1,5]])

D = (A + 3*B.T)*(3*A.T - B)
X = np.dot(np.linalg.inv(D),C)
print(X)
print('Проверка')
print('C =', C)
print('Результат проверки')
print(np.dot(D,X))