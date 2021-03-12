import numpy as np
from scipy import linalg
from math import sin, exp, cos
import matplotlib.pylab as plt


def func(x):
    return sin(x / 5.) * exp(x / 10.) + 5 * exp(-x / 2.)


arr_cord = np.arange(1., 15., 0.1)
arr_func = np.array([func(coord) for coord in arr_cord])

# СЛАУ восьмої степені в т. 1,3,5,7,9,11,13,15
print('\n# СЛАУ восьмої степені в т. 1,3,5,7,9,11,13,15')

arr_cord8 = np.array([1, 3, 5, 7, 9, 11, 13, 15])
N = 8
arrA8 = np.empty((0, N))
for i in range(N):
    arrA8line = list()
    for j in range(N):
        arrA8line.append(arr_cord8[i] ** j)
    arrA8 = np.append(arrA8, np.array([arrA8line]), axis=0)

arrB8 = np.array([func(coord) for coord in arr_cord8])

print(f'arr_cord8: {arr_cord8}')
print(f'arrA8: {arrA8}')
print(f'arrB8: {arrB8}')

arrX8 = linalg.solve(arrA8, arrB8)
print(f'arrX8: {arrX8}')


def func8(x):
    return arrX8[0] + arrX8[1] * x + arrX8[2] * (x ** 2) + arrX8[3] * (x ** 3) + arrX8[4] * (x ** 4) + arrX8[5] * (
            x ** 5) + arrX8[6] * (x ** 6) + arrX8[7] * (x ** 7)


arr_func8 = np.array([func8(coord) for coord in arr_cord])

plt.plot(arr_cord, arr_func8, label='approximation')
plt.scatter(arr_cord, arr_func, alpha=0.5, label='raw function')

plt.title('Approximation')
plt.grid()
plt.legend()
plt.savefig('approximation')
plt.show()