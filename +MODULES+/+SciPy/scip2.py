import numpy as np
from scipy import optimize
from colorama import init, Fore

init()

print(Fore.GREEN, 'Rosenbrok func')
W = np.array([2, 2])


def f(x):
    return 0.5 * (1 - x[0]) ** 2 + (x[1] - x[0] ** 2) ** 2


print(' ', f([1, 1]))

print('\nМетод перебору:\n', optimize.brute(f, ((-5, 5), (-5, 5))))
print('\nМетод диференціальної еволюції:\n', optimize.differential_evolution(f, ((-5, 5), (-5, 5))))

# --------------------------------------------
print('\nGRADIENT func')


def g(x):
    return np.array((-2 * .5 * (1 - x[0]) - 4 * x[0] * (x[1] - x[0] ** 2), 2 * (x[1] - x[0] ** 2)))


print('Оцінка розходження градінта:\n', optimize.check_grad(f, g, W), '- досить мала, тому і вірна\n')

# ---------------------------------------------
print('Ще один варіант знаходження градінта:')
print(optimize.fmin_bfgs(f, W, fprime=g))

# ---------------------------------------------
print('\nЩе один варіант:\n', optimize.minimize(f, W))

# ---------------------------------------------
print('\nПошук максимуму ф-ції f(x): ')


def h(x):
    return -f(x)


print(optimize.minimize(h, W/2))

# ---------------------------------------------
print('\nЩе один варіант (через method="BFGS"):\n', optimize.minimize(f, W, method='BFGS'))
print('\nЩе один варіант (через method="Nelder-Mead"):\n', optimize.minimize(f, W, method='Nelder-Mead'))
