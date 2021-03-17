from numpy.lib.scimath import sqrt
from numpy import exp, linspace, array, arange
import matplotlib.pyplot as plt

# Nuclear reactions in stars
print('Перевірка роботи вікон Гамова\n'.upper())

z1 = 1
z2 = 6

m1 = 1
m2 = 12
A = m1 * m2 / (m1 + m2)

T9 = 0.03
kT = 2.5875 * pow(10, -3)

E0 = 0.122 * pow(z1 ** 2 * z2 ** 2 * A, 1 / 3) * pow(T9, 2 / 3)
DE = 0.2368 * pow(z1 ** 2 * z2 ** 2 * A, 1 / 6) * pow(T9, 5 / 6)

b = 2 * pow(E0, 3 / 2) / kT

print(f'E0 = {E0}')
print(f'DE = {DE}')
print(f'b = {b}\n')


def fun(E):
    return pow(10, 19) * exp(-(b / sqrt(E) + E / kT))


x = linspace(pow(10, -30), 2 * E0, 10000)
y = array([fun(E) for E in x])

# print(f'x = {x}')
# print(f'y = {y}')

plt.plot(x, y, linewidth=0.7, color='red')
plt.grid(color='black', linewidth=0.5, linestyle='--')
plt.title('Перевірка роботи вікон Гамова')
plt.xlabel('E, eV')
plt.ylabel('10^19*exp(-(b/sqrt(E)+E/kT))')

plt.savefig('L_3_Mike_Sh(Gamow)')
plt.show()
