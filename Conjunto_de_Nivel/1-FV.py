# Gráfico de Nível

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import*

def f(x,y):
    return x**2 + y**2

x = linspace(-6,6,100)
y = linspace(-6,6,100)
X,Y = meshgrid(x,y)
Z = f(X,Y)


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
c = plt.contour(X,Y,Z,20,linewideths=0.5)
plt.clabel(c, inline=2, fontsize=8)
plt.axis('scaled')

plt.show()