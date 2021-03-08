from scipy import pi, integrate
from numpy.lib.scimath import sqrt
from numpy import exp

# Trapezoidal Rule
# Nuclear reactions in stars
print('Calculation of probabilities of nuclear reactions in stars\nTrapezoidal Rule:'.upper())

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

def f(r):
    """\nTest function (U = 1.6 * pow(10, -13)):"""
    return sqrt(2 * m * (U - E0))


def f_(r):
    """\nMain function (U = (z1 * z2 * pow(e, 2)) / r):"""
    return sqrt(2 * m * ((z1 * z2 * pow(e, 2)) / r - E0))


a = pow(10, -20)
b = pow(10, -15)
n = 100000
h = (b - a) / n

S = 0.5 * (f(a) + f(b))
for i in range(1, n):
    S += f(a + i * h)
I = h * S
print(f.__doc__, f'\nThe result of integration: {I}')
P = exp((-2 / h_) * I)
print(f'Probability: {P}')


S = 0.5 * (f_(a) + f_(b))
for i in range(1, n):
    S += f_(a + i * h)
I_ = h * S
print(f_.__doc__, f'\nThe result of integration: {I_}')
P_ = exp((-2 / h_) * I_)
print(f'Probability: {P_}')
