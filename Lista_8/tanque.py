""" 
Eros Moreira Ferreira
05/06/2024
Resolve uma EDO pelo método de Euler e Runge Kutta
"""
import numpy as np
def Euler(f, t0, tf, x0,N = 50):
    """
    Pelo método de Euler calcula uma aproximação para uma EDO que possui
    apenas uma variável dependente.
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
        xn = x0 + h * f(x0,t0)
        x0 = xn
        t0 += h
        x[i] = x0
        t[i] = t0
    return x ,t

def Runge_kutta(dxdt, t0, tf, x0, N = 50):
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
    return x ,t




# EDO que terá aproximação encontrada.
dxdt = lambda h, t: -(0.01 / 0.2)**2 * np.sqrt(2 * 9.81 * h)

# Variáveis para a aproximação.
t0 = 0
tf = 160
N = 8
h0 = 1

# Chama a função que calcula a aproximação de uma EDO e recebe os valores.
h1 ,t1 = Euler(dxdt,t0,tf,h0,N)
h2 ,t2 = Runge_kutta(dxdt,t0,tf,h0,N)

# Solução analítica da EDO para comparar com a aproximação.
a = (0.01 / 0.2)**2 *np.sqrt(2 * 9.81)
ht = lambda h,t: a**2 * t**2 /4 - a * t * np.sqrt(h0) + h0

t = np.linspace(t0,tf,8)
h = ht(h0,t)

# plota os graficos
import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))
plt.plot(t1, h1*100, '-.', label = "Euler", color = "red")
plt.plot(t2, h2*100, '--', label = "Runge Kutta", color = "blue")
plt.plot(t, h*100, label = "Solução Analítica", color = "yellow")
plt.axhline(color = "gray",zorder= 1)
plt.ylabel("h(cm)")
plt.xlabel("t(s)")
plt.title(r"Altura da água de um tanque em função do tempo pela solução da EDO $\frac{dh}{dt} = - \left( \frac{r}{R} \right)^2 \sqrt{2gh}$")
plt.legend()
plt.grid(True)
plt.savefig("tanque.png")
plt.show()
