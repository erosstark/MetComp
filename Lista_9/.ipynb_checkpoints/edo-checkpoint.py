# Calcula uma aproximação para uma EDO de primeira ordem
# dado uma condição inicial.

import numpy as np
import matplotlib.pyplot as plt


#===============================================================================
def EDO(t0,tf,x0,N):
    """
    Calcula uma aproximação para uma EDO.
    É recomendado para EDOs de primeira ordem.
    Args:
        t0 (float): valor de t inicial
        tf (float): valor de t final
        x0 (float): valor de x(t0)
        N (int): número de iterações

    Returns:
        Tuple: duas arrays, t e x, com seus 
        espectivos intervalos.
    """
    h = (tf-t0) / N      # Largura do intervalo.
    t = np.zeros([N+1])  # intervalos em t.
    x = np.zeros([N+1])  # intervalos em x.
    x[0] = x0
    t[0] = t0
    
    # Loop do método de Euler.
    for i in range(1, N+1):
        xn = x0 + h * xt(x0,t0)
        x0 = xn
        t0 += h
        x[i] = x0
        t[i] = t0
    return t,x
#===============================================================================

# EDO que terá aproximação encontrada.
xt = lambda x,t: 6*(x**2)*t

# Variáveis para a aproximação.
t0 = 1
tf = 3
N = 100
xt0 = 1/25

# Chama a função que calcula a aproximação de uma EDO e recebe os valores.
x,y = EDO(t0,tf,xt0,N)

# Solução conhecida da EDO para comparar com a aproximação.

z = np.arange(1,3,0.01)
f = 1/(28-3*z**2)
# Plota os gráficos.
plt.plot(x,y, label = "Aproximçã0", color = "red")
plt.plot(z,f, label = "Função", color = "blue")
plt.axhline(color = "gray",zorder= 1)
plt.legend()
plt.grid(True)
plt.show()

"""
Ajuste o nome das variáveis para serem menos confusas
"""
