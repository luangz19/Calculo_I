import matplotlib.pyplot as plt
import numpy as np

def f(x):
     return 1/x

x = np.linspace(-10,10,1000)
y = f(x)

plt.plot(x,y)
plt.grid()
plt.show()