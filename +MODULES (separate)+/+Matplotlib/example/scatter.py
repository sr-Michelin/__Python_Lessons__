import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')
X = [i for i in range(101)]


def sqr(x):
    return x ** 2


Y = [sqr(i) for i in X]

plt.plot(X, Y, linewidth=0.8)
plt.scatter(X, Y, c='red', s=3)
plt.title("Square Numbers", fontsize=12)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of value", fontsize=12)
plt.tick_params(axis='both', labelsize=12)
plt.axis([0, 10, 0, 100])
plt.savefig('test.jpg', bbox_inches='tight')
plt.show()
