import numpy as np
from colorama import init,Fore
init()

print('{0}Запис вектора'.format(Fore.LIGHTCYAN_EX))
x = [x for x in range(0, 100, 10)]
y = np.array(x)
print('{0}, {1}'.format(y, type(y)))

print('{0}   - відображення зрізу вектора {1} [:3] без ком'.format(y[:3], y))
print('{0} - відображення перших двох елементів вектора {1}'.format(y[[0, 1]], y))
print('{0} - відображення  елементів вектора {1} при умові y[y>45]'.format(y[y > 45], y))
print('{0} - результат множення  в-ра {1} на скаляр [5]'.format(y * 5, y),'\n')

print('Запис матриці')
mat = [[1,0,0],[0,1,0],[0,0,1]]
matrix = np.array(mat)
print(matrix)
print('{0} - елемент матриці з індексами [1,1]'.format(matrix[1,1]))

print(np.arange(0,10,2))
