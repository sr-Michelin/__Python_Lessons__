import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('resRO_4_3.txt', sep='\s+', header=None)
data = pd.DataFrame(data)

x = data[0]
y = data[1]
y_1 = data[2]

plt.title('resRO_4_3')
plt.plot(x, y, linewidth=2, color='red', linestyle=':', label='1')
plt.plot(x, y_1, linewidth=1, color='blue', linestyle='--', label='2')
plt.legend()
plt.grid()
plt.xscale('log')
plt.savefig('resRO_4_3')
plt.show()
