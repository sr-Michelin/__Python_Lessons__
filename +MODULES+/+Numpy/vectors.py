import numpy as np
from numpy.linalg import norm
from scipy.spatial.distance import cdist

a = np.array([1, 0, 1], dtype=int)
b = np.array([True, False, False], dtype=int)
c = np.arange(0, 10, 1, dtype=int)

print(a, type(a))
print(b, type(b))
print(c, type(c))

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

# Перевід в-ра у стовбець
a_ = a.reshape((1, 3))
b_ = b.reshape((1, 3))

# Перевід в-ра у стовбець через np.newaxis
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
