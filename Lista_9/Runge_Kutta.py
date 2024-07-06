# Calcula uma aproximação para uma EDO de primeira ordem
# dado uma condição inicial.

import numpy as np
import matplotlib.pyplot as plt


#===============================================================================
def Runge_kutta(dxdt,t0,tf,x0,N):
    """
    Usa o método de Runge Kutta para calcular uma aproximação para uma EDO
    com apenas uma variável dependente.
    Args:
        dxdt (função): EDO que terá solução aproximada
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
    # Condição inicial.
    x[0] = x0
    t[0] = t0

    # Loop que calcula a função pelo Metodo de Runge Kutta.
    for i in range(1, N+1):
        f0 = dxdt(x0,t0)
        f1 = dxdt(x0 + (h/2)*f0, t0 + h/2)
        f2 = dxdt(x0 + (h/2)*f1, t0 + h/2)
        f3 = dxdt(x0 + h*f2, t0 + h)
        xn = x0 + (h/6) * (f0 + 2*f1 + 2*f2 + f3)     # x[i+1]
        x0 = xn
        t0 += h                                       # t[i+1]
        x[i] = xn
        t[i] = t0
    return t,x

"""
pos olhar a exemplo do exercício, percebi que, apesar de certo,
meu código ficou um pouco confuso devido aos nomes das variáveis
e como atribui os novos valores a elas. 
    O exemplo deixou claro do porque o range ir de 0 a n e atribuir no 
início do loop o t[i+1].
"""
#===============================================================================

# EDO que terá aproximação encontrada.
dxdt = lambda x,t: -2 * x * t

# Variáveis para a aproximação.
ti = 0
tf = 2
N = 10
xti = 1

# Chama a função que calcula a aproximação de uma EDO e recebe os valores.
x,t = Runge_kutta(dxdt,ti,tf,xti,N)

# Solução conhecida da EDO para comparar com a aproximação.

z = np.arange(0,2,0.01)
f = np.e ** (-z ** 2)

# Plota os gráficos.
plt.plot(x,t, label = "Aproximção", color = "red")
plt.plot(z,f, label = "Função", color = "blue")
plt.axhline(color = "gray",zorder= 1)
plt.legend()
plt.grid(True)
plt.show()
"""
Ajuste o nome das variáveis para serem menos confusas
Mude a posição das variáveis na função dxdt
"""
