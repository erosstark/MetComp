""" 
Eros Moreira Ferreira
15/04/2024

Calcula a intercesão das duas funções usando o método de Newton-Raphson
"""

import matplotlib.pyplot as plt
import numpy as np

def NR_raiz(f, df, x0, precisao = 1e-7, limite = 100):
  """
    Calcula a raíz de uma função usando o método de Newton-Raphson.

    Precisao de 10^(-7) casas decimais e o limite máximo
  de iterações e 100.

    A partir de um ponto x0 fornecido, converge para a raíz mais
  próxima desse ponto. O ponto fornecido nao pode zerar a derivada.

    O metodo de Newton Raphson pode resolver casos em que o
  metodo da bisseção falha.

  CONSIDERAÇÕES:
    As vezes pode não convergir para a raíz desejada.
    É importante que o ponto esteja próximo da raíz desejada.
    Nem sempre converge!

    Retorna uma tuple com a raiz e o número de iterações.

  """
  nit = 0
  x = x0 - f(x0) / df(x0)

  # Loop que calcula a raíz.
  while  abs(x-x0 ) > precisao and nit < limite:
    x0 = x
    x = x0 - f(x0) / df(x0)
    nit += 1
  return x0, nit


# 0 = P(x) - Q(x)
f = lambda x: x*np.tan(x) - np.sqrt(16 - x**2)
df = lambda x: np.tan(x) + x*(1/np.cos(x)**2) + x/np.sqrt(16 - x**2)

raiz1 = NR_raiz(f,df, 1.5, precisao=1e-5)
raiz2 = NR_raiz(f,df, 3.5, precisao=1e-5)

print(f"A intersecção das duas funções ocorre em x1 = {raiz1[0]:.5f} e \
x2 ={raiz2[0]:.5f} com {raiz1[1]} e {raiz2[1]} iteracões, respectivamente.")


