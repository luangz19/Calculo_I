from pylab import*
from numpy import*

def f(x):
    return exp(x) 

x = linspace(-10,10,200)
y = f(x)

plot(x,y)
grid()
show()
