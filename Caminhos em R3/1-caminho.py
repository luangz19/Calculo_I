import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

def T(x,y):
    return np.array([x+y,x-y])

def f(t):
    return (t**2,t**2)

t = np.linspace(-np.pi,np.pi,100)
x = np.sin(t)
y = np.cos(t)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot(x,y)
plt.grid()
plt.show()
