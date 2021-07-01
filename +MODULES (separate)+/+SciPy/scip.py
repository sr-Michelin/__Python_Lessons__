from scipy import optimize, linalg
from colorama import init, Fore
import numpy as np

init()


def f(x):
    return (x[0] - 1) ** 3 + (x[1] - 2) ** 2 + 10


print(Fore.LIGHTCYAN_EX, '\nЗначення ф-ції за аргументів [1, 2]: ', f([1, 2]))

x_min = optimize.minimize(f, np.array([1, 1]))  # заданий початковий в-р [1,1]

print('Процес опитмізації ф-ції:\n', x_min, '\n')
print('Процес опитмізації ф-ції (скорочений):\n', x_min.x, '\n')

a = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
b = np.array([1, 1, 1])

x = linalg.solve(a, b)
print('Знаходження розвязку лінійної системи A*x=B:\n', x)

print('Множення матриць:\n', np.dot(a, x))

X = np.random.randn(4, 3)
U, D, V = linalg.svd(X)
print('\nМатриця Х:\n', X)
print('Сингулярний розклад матриці X\n', U.shape, D.shape, V.shape)
print(type(U), type(D), type(V))
