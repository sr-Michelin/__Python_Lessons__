import numpy as np
from scipy import linalg
from math import sin, exp, cos
import matplotlib.pylab as plt


def func(x):
    return sin(x / 5.) * exp(x / 10.) + 5 * exp(-x / 2.)


arr_cord = np.arange(1., 15., 0.1)
arr_func = np.array([func(coord) for coord in arr_cord])

# СЛАУ першої степені
print('\n# СЛАУ першої степені')
arr_cord1 = np.array([1, 15])
N = 2
arrA1 = np.empty((0, N))
for i in range(N):
    arrA1line = list()
    for j in range(N):
        arrA1line.append(arr_cord1[i] ** j)
    arrA1 = np.append(arrA1, np.array([arrA1line]), axis=0)

arrB1 = np.array([func(coord) for coord in arr_cord1])
print(f'arr_cord1: {arr_cord1}')
print(f'arrA1: {arrA1}')
print(f'arrB1: {arrB1}')

arrX1 = linalg.solve(arrA1, arrB1)
print(f'arrX1: {arrX1}')


def func1(x):
    return arrX1[0] + arrX1[1] * x


arr_func1 = np.array([func1(coord) for coord in arr_cord])

plt.plot(arr_cord, arr_func, arr_cord, arr_func1)
plt.show()

# СЛАУ другої степені в т.  1,8,15
print('\n# СЛАУ другої степені в т.  1,8,15')
arr_cord2 = np.array([1, 8, 15])
N = 3
arrA2 = np.empty((0, N))

for i in range(N):
    arrA2line = list()
    for j in range(N):
        arrA2line.append(arr_cord2[i] ** j)
    arrA2 = np.append(arrA2, np.array([arrA2line]), axis=0)

arrB2 = np.array([func(coord) for coord in arr_cord2])

print(arr_cord2)
print(arrA2)
print(arrB2)

arrX2 = linalg.solve(arrA2, arrB2)
print(arrX2)


def func2(x):
    return arrX2[0] + arrX2[1] * x + arrX2[2] * (x ** 2)


arr_func2 = np.array([func2(coord) for coord in arr_cord])
plt.plot(arr_cord, arr_func, arr_cord, arr_func1, arr_cord, arr_func2)
plt.show()

# СЛАУ третьої степені в т. 1,4,10,15
print('\n# СЛАУ третьої степені в т. 1,4,10,15')

arr_cord3 = np.array([1, 4, 10, 15])
N = 4
arrA3 = np.empty((0, N))
for i in range(N):
    arrA3line = list()
    for j in range(N):
        arrA3line.append(arr_cord3[i] ** j)
    arrA3 = np.append(arrA3, np.array([arrA3line]), axis=0)

arrB3 = np.array([func(coord) for coord in arr_cord3])

print(arr_cord3)
print(arrA3)
print(arrB3)

arrX3 = linalg.solve(arrA3, arrB3)
print(arrX3)


def func3(x):
    return arrX3[0] + arrX3[1] * x + arrX3[2] * (x ** 2) + arrX3[3] * (x ** 3)


arr_func3 = np.array([func3(coord) for coord in arr_cord])

plt.plot(arr_cord, arr_func, arr_cord, arr_func1, arr_cord, arr_func2, arr_cord, arr_func3)
plt.show()

# Запис у файл
with open('Task_2.txt', 'w') as f_answer:
    for i in arrX3:
        f_answer.write(str(i) + ' ')

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

print(f'\narr_cord8: {arr_cord8}')
print(f'\narrA8: {arrA8}')
print(f'\narrB8: {arrB8}')

arrX8 = linalg.solve(arrA8, arrB8)
print(f'\narrX8: {arrX8}')


def func8(x):
    return arrX8[0] + arrX8[1] * x + arrX8[2] * (x ** 2) + arrX8[3] * (x ** 3) + arrX8[4] * (x ** 4) + arrX8[5] * (
            x ** 5) + arrX8[6] * (x ** 6) + arrX8[7] * (x ** 7)


arr_func8 = np.array([func8(coord) for coord in arr_cord])

plt.plot(arr_cord, arr_func8, label='approximation')
plt.scatter(arr_cord, arr_func, alpha=0.5, label='raw function')

plt.title('Polynomial approximation [n^8]')
plt.grid()
plt.legend()
plt.savefig('Polynomial approximation [n^8]')
plt.show()