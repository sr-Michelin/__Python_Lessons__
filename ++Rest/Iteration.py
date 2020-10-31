from numpy import fabs, sin, cos

L = pow(10, -6)


def f(x_, x, i):
    while True:
        x_ = sin(x) ** 2 + cos(x) ** 2
        x += L
        i += 1
        if fabs(x_ - x) / x <= L:
            print('\nПошук розв\'язів рівняння кола:')
            print('Після {0} ітерацій знайдено: '.format(i))
            print('|x[new]-x[old]| = {0} '.format(fabs(x_ - x) / x))
            print('x[new] = {0}'.format(x_))
            break


f(L, L, 0)
