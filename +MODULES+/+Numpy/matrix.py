import numpy as np

# Створення матриць
print('\n   Створення матриць')
M1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=None)
M2 = np.eye(5)
M3 = np.ones((5, 5))
M4 = np.array([True, False, True], dtype=int)
M5 = np.arange(0, 9, 1).reshape(3, 3)

print('Найпростіший запис матриці M1:\n{0}'.format(M1))
print('\nЗапис одиничної матриці M2:\n{0}'.format(M2))
print('\nЗапис матриці M3, яка складається лише з одиниць:\n{0}'.format(M3))
print('\nЗапис матриці M4 через boolean:\n{0}'.format(M4))
print('\nЗапис матриці M5 через arange-reshape:\n{0}'.format(M5))

# Індексація матриць
print('\n   Індексація матриць')
print('Елемент матриці M5 з [1,1] = {0}'.format(M5[1, 1]))
print('Перший стовбець матриці М5 = {0}'.format(M5[:, 0]))
print('Перший рядок матриці М5 = {0}'.format(M5[0, :]))
print('Елементи матриці М5 із координатами [[1,0],[0,1]] = {0}'.format(M5[[1, 0], [0, 1]]))

# Вектори, вектор-рядок, вектор-стовбець
print('\n   Вектори, вектор-рядок, вектор-стовбець')
M6 = np.array([[1], [2], [3]])
M7 = np.array([1, 2, 3])
M8 = M7.reshape(1, len(M7))

print('Запис матриці - стовпця (двохвимірного масиву)-\n {0}, {1}, розмірність - {2}'.format(M6, type(M6), M6.shape))
print('\nЗапис  рядка - вектора (одновимірного масиву)-\n {0}, {1}, розмірність - {2}'.format(M7, type(M7), M7.shape),
      '\n  Таким чином демонструється факт того, що вектор-рядок і матриця-рядок є різними об\'єктами в Numpy')
print('  Процес "переводу" вектора-рядка і матрицю-рядок --->  {0} ,розмірність змінилася - {1}'.format(M8, M8.shape))
print('\nТранспонування матриці М5: \n{0}'.format(M5.T))

# Множення матриць
print('\n  Множення матриць')
print('Перший метод множення матриць (через np.dot(a,b)): \n{0}\nє еквівалентним другому (a.dot(b)): \n{1}'.format(
    np.dot(M1, M5), M1.dot(M5)))
print('Множення матриці M5 на вектор M7 : \n{0}'.format(M5.dot(M7)))
print('Покоординатне множення матриці M5 на вектор M7 : \n{0}'.format(M5 * M7))

# Транспонування матриць
print('\n  Транспонування матриць')
print('Транспонування матриці M5 методом np.transpose: \n{0}'.format(np.transpose(M5)))
print('Транспонування матриці M5 методом a.T: \n{0}'.format(M5.T))

# Пошук визначника матриць
print('\n  Пошук визначника матриць')
print('Визначник матриці М5 = {0}'.format(np.linalg.det(M5)))

# Пошук рангу матриць
print('\n  Пошук рангу матриць')
print('Ранг матриці М5 = {0}'.format(np.linalg.matrix_rank(M5)))

# Перевірка на лінійну незалежність системи векторів через ранг
print('\n  Перевірка на лінійну незалежність системи векторів через ранг: ', end='')
a = np.array([1, 2, 3])
b = np.array([1, 1, 1])
c = np.array([2, 6, 8])
M = np.array([a, b, c])
print(np.linalg.matrix_rank(M) == M.shape[0])  # m.shape[0] - число векторів

# Системи лінійних рівняннь
print('\n   Системи лінійних рівняннь')
a = np.array([[1, 2], [4, 5]], dtype=int)
b = np.array([1, 0], dtype=int)
x = np.linalg.solve(a, b)
print('Розв\'язок системи Ax = b: ', x)
print('Переконуємся у правильності отриманого результату: b = {0}'.format(a.dot(x)))

a = np.array([[0, 1], [1, 1], [2, 1], [3, 1]])
b = np.array([-1, 0.2, 0.9, 2.1])
x, res, r, s = np.linalg.lstsq(a, b)
print('\nПсевдовирішення лінійних рівнянь [‖𝐴𝑥−𝑏‖^2 --> 0]: {0}'.format(x))

# Зворотні матриці:
print('\n   Зворотні матриці:')
a = np.array([[1, 2, 1], [1, 1, 4], [2, 3, 6]])
b = np.linalg.inv(a)
print(b)
print('Множення матриці на звортню:\n', a.dot(b))

# Власні значення і власні вектори матриці:
print('\n   Власні значення і власні вектори матриці:')
a = np.array([[-1, 0, 0], [0, -2, 0], [0, 0, -3]])
w, v = np.linalg.eig(a)
print('Матриця:\n', a)
print('Власні значення:', w)
print('Власні вектори:\n', v)

# Комплексні числа
print('\nКомплексні числа:')
a = 1j + 10
b = 1j * 1j
print(a, b)

c = a * a
d = a / b
print(c, d)
