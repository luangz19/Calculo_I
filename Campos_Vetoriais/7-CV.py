import matplotlib.pyplot as plt
from numpy import*

x = linspace(-5,5,10)
y = linspace(-5,5,10)

x1,y1 = meshgrid(x,y)

u = -y1**2/((x1**4 + y1**4))**(1/2)
v = x1/((x1**2 + y1**2)**(1/2))

fig = plt.figure(figsize=(10,10))

plt.quiver(x1,y1,u,v)
plt.grid()
plt.show()