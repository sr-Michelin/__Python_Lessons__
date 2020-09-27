import  numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10,0.01)

fig1 = plt.figure(1)
plt.title ('y = (x+1)^(1/x)')
#plt.axis ([-1,2,-1,1])
plt.plot(x,(x+1)**(1/x))

fig2 = plt.figure(2)
plt.plot(x,np.cos(x))

plt.show()

