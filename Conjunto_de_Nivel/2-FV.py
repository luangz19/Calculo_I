import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import*

# f(t) = (x + a*cos(t), y + b*sin(t))

t = linspace(0,2*pi,50)
x = 1 + 3*cos(t)
y = 1 + 4*sin(t)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111,projection='3d')
ax.plot(x,y)
plt.show()