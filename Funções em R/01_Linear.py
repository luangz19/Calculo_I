import matplotlib.pyplot as plt
from pylab import arange

def funcao_afim(x):
    x = 2*x
    return x
x = arange(1,10,0.2)
y = funcao_afim(x)

plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
plt.show()
