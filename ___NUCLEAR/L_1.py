from scipy import pi, integrate
from numpy.lib.scimath import sqrt
from numpy import exp

# Nuclear reactions in stars
print('Calculation of probabilities of nuclear reactions in stars\n'.upper())

# photon mass
m = 1.67 * pow(10, -27)

# quantum planck constant
h_ = (6.626 * pow(10, -34)) / (2 * pi)

# limits of integration
r0 = 0
rm = pow(10, -15)
# rm = float(input('Enter the upper limit of the integration: '))

# elementary charge of an electron
e = 1.6021766208 * pow(10, -19)

# proton number (ordinal number) of elements of nuclear reaction
z1 = 1
z2 = 1

# Energy 1eV = 1,6022e-19 J
E0 = pow(10, -16)
U = 1.6022 * pow(10, -13)

z1 = float(input('Enter the proton number of element I: '))
z2 = float(input('Enter the proton number of element II: '))
E0 = float(input('Enter energy E0 [KeV]: ')) * pow(10, -16)


def fun(r):
    """\nTest function (U = 1.6 * pow(10, -13)):"""
    return sqrt(2 * m * (U - E0))


def func(r):
    """\nMain function (U = (z1 * z2 * pow(e, 2)) / r):"""
    return sqrt(2 * m * ((z1 * z2 * pow(e, 2)) / r - E0))


if __name__ == '__main__':
    # inter_t = integrate.quadrature(fun, r0, rm) # - with 1j
    inter_t = integrate.fixed_quad(fun, r0, rm)
    print(fun.__doc__, f'\nThe result of integration: {inter_t[0]}')
    P = exp((-2 / h_) * inter_t[0])
    print(f'Probability: {P}')

    inter_m = integrate.quadrature(func, r0, rm)
    print(func.__doc__, f'\nThe result of integration: {inter_m[1]}')
    P = exp((-2 / h_) * inter_m[1])
    print(f'Probability: {P.real}')

input()
