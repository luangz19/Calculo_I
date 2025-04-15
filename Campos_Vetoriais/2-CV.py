import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import*

x = arange(-1,1,0.25)
y = arange(-1,1,0.25)
z = arange(-1,1,0.25)

xi,yi,zi = meshgrid(x,y,z)

u = sin(xi)*cos(yi*zi)
v = -yi*zi
w = cos(xi)*sin(zi)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(xi,yi,zi,u,v,w, length=0.2, linewidths=0.7, color='black')
plt.show()