from numpy.lib.scimath import sqrt
from numpy import exp, linspace, array, arange
import matplotlib.pyplot as plt

# Nuclear reactions in stars
print('Перевірка роботи вікон Гамова\n'.upper())

S = ['p + 12C', 'p + p', 'd + p', '3He + 3He', '3He + 4He', '7Be + e-', '7Li + p', '3He + 4He', '7Be + p']

Z1 = [1, 1, 1, 2, 2, 4, 3, 2, 4]
Z2 = [6, 1, 1, 2, 2, -1, 1, 2, 1]

M1 = [1, 1, 1, 3, 3, 7, 7, 3, 7]
M2 = [12, 1, 2, 3, 4, 5.447 * pow(10, -4), 1, 4, 1]

T9_ = 14  # 14 KK

T9 = T9_ / pow(10, 3)
k = 8.617 * pow(10, -5)
kT = k * T9_

i = 1
for m_1, m_2, z_1, z_2, s_1 in zip(M1, M2, Z1, Z2, S):
    A = m_1 * m_2 / (m_1 + m_2)
    E0 = 0.122 * pow(z_1 ** 2 * z_2 ** 2 * A, 1 / 3) * pow(T9, 2 / 3)
    DE = 0.2368 * pow(z_1 ** 2 * z_2 ** 2 * A, 1 / 6) * pow(T9, 5 / 6)

    b = 2 * pow(E0, 3 / 2) / kT

    print(f'Д {i}: {s_1}')
    print(f'{kT=}')
    print(f'{m_1=}, {m_2=}, {z_1=}, {z_2=}')
    print(f'E0 = {E0}')
    print(f'DE = {DE}')
    print(f'b = {b}\n')


    def fun(E):
        return pow(10, 19) * exp(-(b / sqrt(E) + E / kT))


    x = linspace(pow(10, -30), 2 * E0, 10000)
    y = array([fun(E) for E in x])

    plt.figure(figsize=(10, 7))
    plt.plot(x, y, linewidth=0.8, color='red')
    plt.grid(color='black', linewidth=0.5, linestyle='--')
    plt.title(f'Gamow {i}: {s_1}')
    plt.figtext(0.5, 0.02, f'E0 = {round(E0, 5)} eV , DE = {round(DE, 5)} eV, b ={round(b, 5)}',
                fontsize=10 , horizontalalignment ="center")
    plt.xlabel('E, eV',fontsize=10)
    plt.ylabel('10^19*exp(-(b/sqrt(E)+E/kT))',fontsize=10)
    plt.savefig(f'Gw {i} -- {s_1}')
    plt.show()
    i += 1
