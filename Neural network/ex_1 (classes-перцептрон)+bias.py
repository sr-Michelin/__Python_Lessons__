import numpy as np
import matplotlib.pyplot as plt

N = 5
b = 3  # bias - зміщення

# Клас С1
x1 = np.random.random(N)
x2 = x1 + [np.random.randint(10) / 10 for i in range(N)] + b
C1 = [x1, x2]

# Клас С2
x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10) / 10 for n in range(N)] - .1 + b
C2 = [x1, x2]

f = [0 + b, 1 + b]  # пряма pi/4 + bias

w2 = 0.5
w3 = -b * w2
w = np.array([-w2, w2, w3])  # ваги для нейроної мережі

for i in range(N):
    x = np.array([C1[0][i], C1[1][i], 1])
    y = np.dot(w, x)

    if y >= 0:
        print('Клас C1')
    else:
        print('Клас C2')

plt.scatter(C1[0][:], C1[1][:], s=10, c='red')
plt.scatter(C2[0][:], C2[1][:], s=10, c='blue')
plt.plot(f)
plt.grid(True)
plt.show()
