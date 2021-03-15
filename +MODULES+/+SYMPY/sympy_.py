from sympy import symbols, integrate, diff, sin, cos

x = symbols('x')


def f(x):
    return 3 * sin(x) + cos(x)


def Df(x):
    """Похідна від f(x)"""
    Df = diff(f(x))
    print(f'Похідна: {Df}')
    return Df


def df(x):
    """Первісна від f(x)"""
    df = integrate(f(x))
    print(f'Первісна: {df}')
    return df


Df(x)
df(x)
