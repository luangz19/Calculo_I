import matplotlib.pyplot as plt
import numpy as np

def f(x,a,b,c):
    return a*x**2 + b*x + c

x = np.linspace(-20,20,1000)

y = f(x,-4,7,4)

plt.plot(x,y)
plt.grid()
plt.show()