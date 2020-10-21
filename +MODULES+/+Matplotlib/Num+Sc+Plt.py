import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from colorama import init, Fore

init()

x = np.arange(-10, 10, 0.1)
y = np.exp(- x / 3.0) + np.random.randn(
    len(x)) * 0.5  # доданок {np.random.randn(len(x)) * 0.08} вказує на наявність шумів у ф-ції

print(Fore.GREEN, end='')
print('Запис трьох перших значень Х: \n', x[:3])
print('Запис трьох перших значень Y: \n', y[:3])

# f = interpolate.interp1d(x,y,kind='linear')
f = interpolate.interp1d(x, y, kind='quadratic')
x_new = np.arange(0, 9, 1)
y_new = f(x_new)

plt.plot(x, y, 'o', x_new, y_new, '-')
plt.show()
