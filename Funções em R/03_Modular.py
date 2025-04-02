import matplotlib.pyplot as plt
from numpy import*

x = linspace(-10,10,50)
y = abs(x)

plt.plot(x,y)
plt.grid()
plt.show()
