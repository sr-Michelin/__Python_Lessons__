# ввід та вивід векторів
from network import Network

net = Network(10, 5, 5)
net.run([1, .5, .1, .2, .7, .9, 1, .6, .3, .1])
out = net.output()
print(out)
