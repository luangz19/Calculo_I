import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import*

# Sela ou paraboloide de hiperpolico

def f(x,y):
    return y**2 - x**2

x = linspace(-4,4,50)
y = linspace(-4,4,50)

X,Y = meshgrid(x,y)
Z = f(X,Y)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
c = ax.contour(X,Y,Z, 20, linewidths=0.5)
ax.clabel(c, inline=2, fontsize=8 )
plt.axis('scaled')
plt.show()