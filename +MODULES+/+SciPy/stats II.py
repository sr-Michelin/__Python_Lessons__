import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts
from collections import Counter

# -------------------------------
# Дискретний розподіл
print('\nДискретний розподіл')
# Підкидування кубика 100 разів
N = 10000
sample = np.random.choice([1, 2, 3, 4, 5, 6], N)
c = Counter(sample)
print('Число випадів кожної зі сторін: {}'.format(c))

# Отримаєм вірогідності
print('Вірогідності кожної із сторін: ', end='')
print({k: v / N for k, v in c.items()})

# -------------------------------
# Неперервний розподіл
N = 100
print('\nНеперервний розподіл')
# Готуємо вибірку обєму N нормального розподілу (mu = 0, sigma^2 = 1)
norm_rv = sts.norm(0, 1)
sample = norm_rv.rvs(N)

# Готуємо емпіричну ф-цію розподілу
x = np.linspace(-4, 4, N)
y = norm_rv.cdf(x)
plt.plot(x, y, label='theoretical CDF')

from statsmodels.distributions.empirical_distribution import ECDF

ecdf = ECDF(sample)
plt.step(ecdf.x, ecdf.y, label='ECDF')
plt.legend()
plt.title("Неперервний розподіл")

plt.legend(loc='upper left')
plt.ylabel('$f(x)$')
plt.xlabel('$x$')
plt.show()

# Гістограма вибірки
plt.hist(sample, bins=40)

plt.title("Гістограма вибірки неперервного розподілу")

plt.ylabel('fraction of samples')
plt.xlabel('$x$')
plt.show()

# Ядерне зглажування
print('\nЯдерне зглажування')
df = pd.DataFrame(sample, columns=['KDE'])
ax = df.plot(kind='density')

# тут же будуєм побудуєм теоретичну густину розподілу
y = norm_rv.pdf(x)
plt.plot(x, y, label='theoretical pdf', alpha=0.5)

plt.legend()
plt.title("Ядерне зглажування")

plt.ylabel('$f(x)$')
plt.xlabel('$x$')
plt.show()
