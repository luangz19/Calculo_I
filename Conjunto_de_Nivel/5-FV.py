import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import*

# Efera S²(a) = {(x,y,z); x² + y² + z² = a²} em R³

def f(x,y):
    return (4 - x**2 - y**2)**(1/2) # onde a² = 4 e considerando a Z = f(x,y)

def g(x,y):
    return -(4 - x**2 - y**2)**(1/2) # onde a² = 4 e considerando a Z = f(x,y)

x = linspace(-4,4,1000)
y = linspace(-4,4,1000)
X,Y = meshgrid(x,y)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X,Y,f(X,Y), alpha=0.5)
ax.plot_surface(X,Y,g(X,Y), alpha=0.5)

plt.show()