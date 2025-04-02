import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.where(x > 0, x + 1, 1)  # Usa np.where para operar em arrays

x = np.linspace(-10, 10, 1000)  # Gera 1000 pontos entre -10 e 10
y = f(x)  # Avalia a função em todos os pontos de x

plt.plot(x, y)
plt.grid()
plt.show()

    