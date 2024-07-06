"""
Função que implementa método de Runge-Kutta de 4a ordem para uma ODE
Versão para uma única equação.
"""
import numpy as np

def RungeKutta4(f, xi, ti, tf, n):
    """
    Método de Runge-Kutta de 4a ordem para x'= f(x,t), x(0) = xi, com n passos de ti até tf
    Em seu programa faça 
       "from rk4 import RungeKutta4"
    e chame a função RungeKutta4 na forma
       "x, t = RungeKutta4(f, xi, ti, tf, n)"
    onde t são os pontos da variável independente e x os respectivos valores da variável dependente.
    """
    t = np.zeros(n+1)  # n+1 pontos para incluir o tf
    x = np.zeros(n+1)  #x[i] eh a solucao no tempo t[i]
    t[0] = ti
    x[0] = xi   # Condição inicial
    h = float(tf-ti)/n
    for i in range(n):
        #print (i, t[i], x[i], f(x[i]) )  # Passos intermediários, para testes
        t[i+1] = t[i] + h
        f0 = f(x[i], t[i])
        f1 = f(x[i]+h/2*f0, t[i]+h/2)
        f2 = f(x[i]+h/2*f1, t[i]+h/2)
        f3 = f(x[i]+h*f2, t[i] + h)
        x[i+1] = x[i] + h/6*(f0 + 2*f1 + 2*f2 + f3)
    return x, t

