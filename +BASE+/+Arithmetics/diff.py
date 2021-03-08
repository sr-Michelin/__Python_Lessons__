from sympy import sqrt, integrate, symbols, pi, diff

t = symbols('t')
f = 2 ** t
df = diff(f)
print('diff({0}) = {1}'.format(f, df))

# -----------------------------------------------------------------------
r = symbols('r')
m = 1.67 * pow(10, -27)
rm = pow(10, -15)
e = 1.6021766208 * pow(10, -19)
h = (6.626 * pow(10, -34)) / (2 * pi)
z1 = 1
z2 = 1
E0 = 1000

f = sqrt(2 * m * (z1 * z2 * pow(e, 2) / r - E0))
df = integrate(f)

print('{}'.format(df))


def func(r):
    return exp((-2 / h) * (1.82756668824971e-12 * Piecewise((1.0 * 1j * r ** (3 / 2) / sqrt(
        r - 2.56696992423811e-41) - 2.56696992423811e-41 * 1j * sqrt(r) / sqrt(
        r - 2.56696992423811e-41) - 2.56696992423811e-41 * 1j * acosh(1.97373848745177e+20 * sqrt(r)),
                                                             3.8956436168484e+40 * Abs(r) > 1), (
                                                                -1.0 * r ** (3 / 2) / sqrt(
                                                                    2.56696992423811e-41 - r) + 2.56696992423811e-41 * sqrt(
                                                                    r) / sqrt(
                                                                    2.56696992423811e-41 - r) + 2.56696992423811e-41 * asin(
                                                                    1.97373848745177e+20 * sqrt(r)), True))))

# print(func(rm))
