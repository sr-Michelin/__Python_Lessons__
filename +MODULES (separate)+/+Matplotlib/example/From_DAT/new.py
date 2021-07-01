import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(-10, 10, 100)

plt.subplot(211)


def f1(x):
    return np.cos(x)


y_1 = np.array([f1(x) for x in x_1])

plt.title('f1(x)')
plt.plot(x_1, y_1, color='black', linewidth=0.4)
plt.scatter(x_1, y_1, color='red', s=3)

# --------------------------------------------
plt.subplot(212)


def f2(x):
    return np.sin(x)


y_2 = np.array([f2(x) for x in x_1])
plt.title('f2(x)')
plt.plot(x_1, y_2, color='black', linewidth=0.4)
plt.scatter(x_1, y_2, color='blue', s=3)
plt.show()
