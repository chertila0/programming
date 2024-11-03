import matplotlib.pyplot as plt

# Определим координаты точек
A = (0, 0)
B = (0, 2)
C = (1, 1)

# Создаём массивы x и y для построения ломаной
x = [A[0], B[0], C[0]]
y = [A[1], B[1], C[1]]

# Создаём график
plt.plot(x, y, marker='o')

# Подписываем точки
plt.text(A[0] - 0.1, A[1] - 0.1, 'A(0,0)', fontsize=12)
plt.text(B[0] - 0.1, B[1] + 0.1, 'B(0,2)', fontsize=12)
plt.text(C[0] + 0.05, C[1] - 0.1, 'C(1,1)', fontsize=12)

# Подписываем оси
plt.xlabel('x')
plt.ylabel('y')

# Устанавливаем границы графика
plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 2.5)

# Показываем сетку
plt.grid()

# Показываем график
plt.title('Кривая ABC')
plt.show()