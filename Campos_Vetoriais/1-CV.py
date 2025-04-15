import matplotlib.pyplot as plt
from numpy import*

# Campo vetorial bidimensional
# É uma relação f:R² → R² em que o domínio é um subconjunto
# de R² e a imagem é um conjunto de vetores no plano, ou seja,
# uma função que associa, a cada ponto (x,y) do domínio, um
# único vetor (u,v). Podemos escrever
# f (x, y) = (u,v)

# f(x,y) = (u,v)

x = linspace(-5,5,10)
y = linspace(-5,5,10)
x1,y1 = meshgrid(x,y)

u = -y1
v = x1

fig = plt.figure(figsize=(10,10))
plt.quiver(x1,y1,u,v, color='g')
plt.grid()
plt.show()