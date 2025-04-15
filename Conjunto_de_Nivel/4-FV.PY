import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import*

# Élise Circular
# f(t) = (acos(t),asen(t)), onde a > 0

t = linspace(-pi,2*pi,50)
x = 2*cos(t)
y = 2*sin(t)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y)
ax.set(xlabel='x', ylabel='y', zlabel='z')
plt.show()