import numpy as np
import time
import matplotlib.pyplot as plt

'''plt.plot([1,2,3,5],[1,3,4,5])
plt.show()'''

while True:
    x = np.arange(-10, 10, 0.1)
    y = x ** 4/1000 + np.random.randn(len(x)*1)

    for i in  np.arange(21):
        circl_1 = plt.Circle((0+np.random.randint(-10.,10.),0+np.random.randint(0.,10.)),0.2)
        ax = plt.gca()
        ax.add_patch(circl_1)

    plt.plot(x, y)
    plt.show()


