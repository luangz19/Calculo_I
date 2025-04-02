import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x,y):
    return x + y


x = np.linspace(-2, 2, 30)
y = np.linspace(-2, 2, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)


fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')  
ax.plot_surface(X ,Y, Z, alpha=0.5)
ax.plot_wireframe(X, Y, Z, lw=0.5, alpha=0.5)
ax.set(xlabel = 'x', ylabel = 'y', zlabel = 'z')
#ax.set_zlim(0,8)
ax.plot([-2, 2], [0, 0], [0, 0], color='red', linewidth=2) 
ax.plot([0, 0], [-2, 2], [0, 0], color='green', linewidth=2) 
ax.plot([0, 0], [0, 0], [-2, 2], color='blue', linewidth=2)
#ax.set_title(r"$f(x, y) = x + y$")
plt.show()
