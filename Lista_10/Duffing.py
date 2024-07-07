"""
Eros Moreira Ferreira

Resolveno a equação de Duffing para um sistema massa-mola.
A equação de Duffing esta na forma de sistema de eq diferenciais acopladas.

dx/dt = vx
dvx/dt = -δvx - αx - βx^3 + γcos(ωt)

"""


import numpy as np
import matplotlib.pyplot as plt
from euler_syst import Euler
from rk4 import RungeKutta4

############################################################################################
# CASO 1
############################################################################################

# Função da equação de Duffing
def duffing(s,t):

    α = 1.2
    δ = 0.2
    ω = 0
    γ = 0
    β = 0
    return np.array([s[1], -δ*s[1] - α*s[0] - β*s[0]**3 + γ*np.cos(ω*t)])

# Solução analítca da equação de Duffing.

def solution(x0, t):
    α = 1.2
    δ = 0.2
    return x0 * np.exp(-δ*t / 2) * np.cos(np.sqrt(α) * t)

# Parâmetros da equação de Duffing

# Condições iniciais
ti = 0
tf = 30
x0 = 1
v0 = 0

# Numerical solution    
Se1, te1 = Euler(duffing, [x0, v0], ti, tf, 1000)
Sr1, tr1 = RungeKutta4(duffing, [x0, v0], ti, tf, 1000)


# Analytical solution
t = np.linspace(ti, tf, 100)
x = solution(x0, t)

# plot results.
plt.figure()
plt.plot(te1, Se1[:,0], 'r', label = 'Numerical solution Euler')
plt.plot(t, x, 'b', label = 'Analytical solution')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.savefig("Duffing_euler_caso1.pdf")

plt.figure()
plt.plot(tr1, Sr1[:,0], 'r', label = 'Numerical solution Runge-Kutta')
plt.plot(t, x, 'b', label = 'Analytical solution')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.savefig("Duffing_RK_caso1.pdf")

plt.show()

############################################################################################
# CASO 2
############################################################################################

def duffing2(s,t):

    α = -1
    δ = 0.3
    ω = 1.2
    γ = 0.5
    β = 1
    return np.array([s[1], -δ*s[1] - α*s[0] - β*s[0]**3 + γ*np.cos(ω*t)])

# Condições iniciais.

ti = 0
tf = 260
x0 = 1
v0 = 0

# Numerical solution.

Se2, te2 = Euler(duffing2, [x0, v0], ti, tf, 10000)
Sr2, tr2 = RungeKutta4(duffing2, [x0, v0], ti, tf, 10000)
# sr = [x, vx]


# Plot dos resultados.
# V(x)
plt.figure()
plt.plot(Se2[:,0], Se2[:,1], 'b', label = 'Numerical solution Euler')
plt.plot(Sr2[:,0], Sr2[:,1], 'r', label = 'Numerical solution Runge-Kutta')
plt.xlabel('x')
plt.ylabel('v')
plt.legend()
plt.savefig("Duffing_Vx_caso2.pdf")

# x(t)
plt.figure()
plt.plot(te2, Se2[:,0], "b", label = "Numerical solution Euler")
plt.plot(tr2, Sr2[:,0], "r", label = "Numerical solution Runge-Kutta" )
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.savefig("Duffing_xt_caso2.pdf")

plt.show()
