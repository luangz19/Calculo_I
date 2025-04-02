import matplotlib.pyplot as plt
import numpy as np

def f(x,a,b):
    return a*x + b

x = np.linspace(-2,10, 1000)

y = f(x,2,-3)

plt.plot(x,y)
plt.grid()
plt.show()