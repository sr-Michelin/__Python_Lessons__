import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts

# --------------------------------- 
# Нормальний розподіл (Gauss)
print('\nНормальний розподіл (Gauss)')
u = 5
sigma = 0.1

norm_rv = sts.norm(loc=u, scale=sigma)  # задаємо нормальну величну із параметрами u і sigma
print('Певна кількість елементів: ', norm_rv.rvs(size=5))  # генеруємо певну кількість елементів
print('Значення ф-ції норм. розп. в тоці [3]: ', norm_rv.cdf(3))

# Простенький графік ф-ції розподілу Гауса
x = np.linspace(0., 10., 1000)
y = norm_rv.cdf(x)
# plt.plot(x, y)
plt.ylabel('$F(x)$')
plt.xlabel('$x$')
# plt.show()

# Графік ф-ції густини розподілу Гауса
x1 = np.linspace(0., 10., 1000)
y1 = norm_rv.pdf(x)
# plt.plot(x1, y1)
plt.ylabel('$f(x)$')
plt.xlabel('$x$')
# plt.show()

# ---------------------------------------
# Рівномірний розподіл випадкової величини
print('\nРівномірний розподіл випадкової величини')
a = 1
b = 10
unif_rv = sts.uniform(a, b - a)
print('Певна кількість елементів:', unif_rv.rvs(5))

# Графік ф-ції рівномірного розподілу
x = np.linspace(0, 10, 1000)
y = unif_rv.cdf(x)
# plt.plot(x, y)
plt.ylabel('$F(x)$')
plt.xlabel('$x$')
# plt.show()

# Графік ф-ції густини розподілу рівномірного розподілу
y1 = unif_rv.pdf(x)
# plt.plot(x, y1)
plt.ylabel('$f(x)$')
plt.xlabel('$x$')
# plt.show()

# ---------------------------------------
# Розподіл Бернулі (значення [0] або [1])
print('\nРозподіл Бернулі')
ber_rv = sts.bernoulli(0.7)
print('Певна кількість елементів:', ber_rv.rvs(5))

# ---------------------------------------
# Біномний розподіл
print('\nБіномний розподіл')
binom_rv = sts.binom(20, 0.7)  # n,P
print('Певна кількість елементів:', binom_rv.rvs(5))

# Графік ф-ції біномного розподілу
x = np.linspace(0, 20, 21)
y = binom_rv.cdf(x)
# plt.plot(x, y)
plt.ylabel('$F(x)$')
plt.xlabel('$x$')
# plt.show()

# Графік ф-ції густини розподілу біномного розподілу
x1 = np.linspace(0, 20, 21)
y1 = binom_rv.pmf(x)
# plt.plot(x1, y1, '+')
plt.ylabel('$P(X=x)$')
plt.xlabel('$x$')
# plt.show()

# Експеримент ф-ції біномного розподілу
x = np.linspace(0, 45, 46)
for N in [20, 30, 40]:
    for p in [0.2, 0.7]:
        rv = sts.binom(N, p)
        y = rv.cdf(x)
        # plt.step(x, y, label="$N=%s, p=%s$" % (N, p))
plt.legend()
plt.title("CDF (binomial)")
plt.ylabel('$F(X)$')
plt.xlabel('$x$')
# plt.show()

# Експеримент ф-ції густини розподілу біномного розподілу
x = np.linspace(0, 45, 46)
symb = iter(['o', 's', '^', '+'])
for N in [20, 30]:
    for p in [0.2, 0.8]:
        rv = sts.binom(N, p)
        y = rv.pmf(x)
        # plt.plot(x, y, next(symb), label="$N=%s, p=%s$" % (N, p))
plt.legend()
plt.title("PMF (binomial)")
plt.ylabel('$P(X=x)$')
plt.xlabel('$x$')
# plt.show()

# ---------------------------------------
# Розподіл Пуасона
print('\nРозподіл Пуасона')
pois_rv = sts.poisson(5)
print('Певна кількість елементів:', pois_rv.rvs(5))

# Експеримент ф-ції розподілу Пуасона
x = np.linspace(0, 30, 31)
for l in [1, 5, 10, 15]:
    rv = sts.poisson(l)
    cdf = rv.cdf(x)
    # plt.step(x, cdf, label="$\lambda=%s$" % l)
plt.legend()
plt.title("CDF (poisson)")
plt.ylabel('$F(x)$')
plt.xlabel('$x$')
# plt.show()

# Експеримент  ф-ції густини розподілу Пуасона

x = np.linspace(0, 30, 31)

symbols = iter(['o', 's', '^', '+'])
for l in [1, 5, 10, 15]:
    rv = sts.poisson(l)
    pmf = rv.pmf(x)
    # plt.plot(x, pmf, next(symbols), label="$\lambda=%s$" % l)
plt.legend()
plt.title("PMF (poisson)")
plt.ylabel('$P(X=x)$')
plt.xlabel('$x$')
# plt.show()


# ---------------------------------------
# Дискретний розподіл
print('\nДискретний розподіл')
# Генерація випадкових величин
el = np.array([1, 5, 12])
probab = [0.05, 0.7, 0.25]
n = np.random.choice(el, 10, p=probab)
print(n)

# ---------------------------------------
# Xi^2, k - ступені свободи
print('\nXi^2')
chi2_rv = sts.chi2(20)
print('Певна кількість елементів:', chi2_rv.rvs(5))

x = np.linspace(0, 30, 100)
for k in [0.001, 1, 2, 5, 10, 15, 20, 50]:
    rv = sts.chi2(k)
    y = rv.cdf(x)
    # plt.plot(x, y, label='$k=%s$' % k)
plt.legend()
plt.title("CDF ($\chi^2_k$)")
# plt.show()
