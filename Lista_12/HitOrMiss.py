"""
Eros Moreira Ferreira
28/06/2024

Calcula uma integral pelo método de hit or miss.
"""
import numpy as np

def hitOrMiss(f, a, b, H, N):
    """
    Calcula uma integral pelo método de hit or miss

    Args:
        f (func): função que será integrada
        a (float): limite inferior
        b (float): limite superior
        H (float): altura
        N (int): N pontos a serem sorteados

    Returns:
        tuple: Integral, numero de sorteios aceitos
    """
#    np.random.seed(1)
    N_acertos = 0
    x = np.random.uniform(a, b, N)
    y = np.random.uniform(0, H, N)
    for xi, yi in zip(x, y) :
        if f(xi) >= yi:
            N_acertos +=1
    integral = (b - a) * H * N_acertos / N
    return integral, N_acertos

# Função que será integrada.
fx = lambda x: x**3

a = 0; b = 1 # Limites de integração.
H = 1
Ns = [10_000, 100_000, 1_000_000]
valor_exato = 0.25   # Valor exato da integral

for N in Ns:
    I, aproveitos = hitOrMiss(fx, a, b, H, N)
    erro = abs(I - valor_exato)
    sigma = np.sqrt(I * (((b-a) * H) - I) / N )
    print(f"{N = }\nValor da integral : {I}\nNúmeros aproveitados : {aproveitos}\n\
Erro absoluto : {erro:.6f}\nσ = {sigma:6f}\n")