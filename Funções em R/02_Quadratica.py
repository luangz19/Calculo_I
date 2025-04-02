import matplotlib.pyplot as plt
from pylab import arange
# Dados
def f(x):
   return x**2
x = arange(0,1,0.1)
y = f(x)

# Criar gráfico
plt.plot(x, y)
plt.title('Parábolas y = x²')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Mostrar gráfico
plt.show()
