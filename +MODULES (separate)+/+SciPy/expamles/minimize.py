from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 3


x_arr = np.arange(-10, 10, .5)
y_arr = np.array([f(x) for x in x_arr])

o_m = minimize(f, np.array(1), method='BFGS')
print('Optimize minimize, method=\'BFGS\':\nx = {0}, y = {1} after {2} iterations'.format(float(o_m.x), float(o_m.fun),
                                                                                          o_m.nit))

plt.title('Демонстрація scipy і numpy')
plt.grid()
plt.plot(x_arr, y_arr)
plt.scatter(float(o_m.x), float(o_m.fun), color='#0a0b0c')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig('Optimize minimize, method=\'BFGS\'')
plt.show()