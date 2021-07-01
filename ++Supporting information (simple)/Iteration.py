from numpy import fabs, sin, cos

# L = pow(10, -1)
L = 1


def f(x_, x, i):
    """Програма для пошуку розв\'язків введених рівнянь"""
    while True:
        x_ = sin(x) ** 2 + cos(x) ** 2  # used function
        x += L
        i += 1
        if fabs(x_ - x) / x <= L:
            print('\nПошук розв\'язів рівняння кола:')
            print('Після {0} ітерацій знайдено: '.format(i))
            print('|x[new]-x[old]| = {0} '.format(fabs(x_ - x) / x))
            print('x[new] = {0}'.format(x_))
            break


if __name__ == '__main__':
    print(f.__doc__)
    f(L, L, 0)
