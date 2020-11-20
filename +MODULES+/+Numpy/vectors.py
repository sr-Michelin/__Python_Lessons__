import numpy as np
from numpy.linalg import norm
from scipy.spatial.distance import cdist

a = np.array([1, 0, 1], dtype=int)
b = np.array([True, False, False], dtype=int)
c = np.arange(0, 10, 1, dtype=int)
L = np.linspace(0, 1, 5, endpoint=1)  # 5 точок у відрізку [0,1]
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(L, type(L))

print('Розмірність - {0}, вимірність - {1}'.format(a.shape, a.ndim))

# Операції над векторами
print('\nСума a і b: ', a + b)
print('Різниця a і b: ', a - b)
print('Добуток a і b: ', a * b)

# Норми
print('\nМанхетенська норма в-ра a: {0}'.format(np.linalg.norm(a, ord=1)))
print('Евклідова норма в-ра a: {0}'.format(np.linalg.norm(a, ord=2)))

# Відстань між векторами
print('\nМанхетенська відстань між a i b = {0}'.format(np.linalg.norm(a - b, ord=1)))
print('Евклідова відстань між a i b = {0}'.format(np.linalg.norm(a - b, ord=2)))

# Перевід в-ра у матрицю-рядок
a_ = a.reshape((1, 3))
b_ = b.reshape((1, 3))

# Перевід в-ра у матрицю через np.newaxis
d = np.array([1, 2, -1, 10])
print('{0}, розмірність - {1}'.format(d, d.shape))
print('Вектор {0} з newaxis ---> рядок: {1}, розмірність {2} '.format(d, d[np.newaxis, :], d[np.newaxis, :].shape))
print('Вектор {0} з newaxis ---> стовпець: \n{1}, розмірність {2} '.format(d, d[:, np.newaxis], d[:, np.newaxis].shape))

# Відстань між векторами через  scipy...cdist
print('\nМанхетенська відстань між a i b = {0}  - [cdist]'.format(cdist(a_, b_, metric='cityblock')))
print('Евклідова відстань між a i b = {0}  - [cdist]'.format(
    cdist(a[np.newaxis, :], b[np.newaxis, :], metric='euclidean')))

# Скалярний добуток векторів
print('\nСкалярний добуток a i b = {0}'.format(np.dot(a, b)))
print('Скалярний добуток a i b = {0} -- [a.dot(b)]'.format(a.dot(b)))

# Косинус між векторами a i b [через скалярний добуток]
cos_angle = np.dot(a, b) / (norm(a) * norm(b))
print('Косинус кута між a i b = {0}'.format(cos_angle))
print('Кут між a i b = {0}'.format(np.arccos(cos_angle)))

# Витяг масиву в одну строку // наслідування
_a = a.flatten()  # повертає копію - непряме наслідування
_a_ = np.array(a)  # копія

_b = a.ravel()  # reshape(-1) - не повертає копію - пряме наслідування
_b_ = np.asarray(a)  # пряме наслідування

# Агрегуючі ф-ції
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('\nАгрегуючі ф-ції:\nmin:{0},max:{1}, argmax:{2}, sum: {3}, prod:{4}, mean:{5}'
      .format(a.min(), a.max(), a.argmax(), a.sum(), a.prod(), a.mean()))

a = a.reshape(5, 2)  # двовимірний випадок
print('Двовимірний випадок [min(axis = 0)]:', a.min(axis=0), '- редукція вздовж стопця.')
