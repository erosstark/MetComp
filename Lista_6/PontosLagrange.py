"""
Eros Moreira Ferreira

Calcula a distância r do ponto L1 ao Sol.

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

    Args:
        f (func): função que terá raiz encontrada
        df (func): derivada da função acima
        x0 (float): chute inicial
        precisao (float, optional): precisão relativa. Defaults to 1e-7.
        limite (int, optional): limite máximo de interações. Defaults to 100.

    Returns:
        tuple: raíz e o número de iterações
    """
    nit = 0
    x = x0 - f(x0) / df(x0)

    # Loop que calcula a raíz.
    while  abs(x-x0 ) > precisao and nit < limite:
        x0 = x
        x = x0 - f(x0) / df(x0)
        nit += 1
    return x0, nit




# Constantes utilizadas
R = 1.5e11 # Distância entre a terra e o sol (m)
m = 5.9736e24 # Massa da terra (kg)
M = 1.989e30 # Massa do Sol (kg)
w = 1.992e-7 # Velocidade angular da Terra e do satélite (1/s)
G = 6.674e-11 # Constante de gravidade (m^3 kg^-1 s^-2)

def EqDistancia(r):
    """
    Função cuja raiz é a distância entre L1 e o Sol.
    """
    return G * M / r**2 - G * m / (R - r)**2 - w**2 * r

def Derivada_EqDistancia(r):
    """
    Derivada da EqDistancia em relação a x.
    """
    return -2 * G * M / r**3 + 2 * G * m / (R - r)**2 - w**2

