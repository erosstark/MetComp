""" 
Eros Moreira Ferreira
28/06/2024

Calcula uma integral pelo método da media 
"""
import numpy as np
def intMedia(f, a, b, N):
    """
    Calcula uma integral pelo método da media

    Args:
        f (func): função que será integrada
        a (float): limite inferior
        b (float): limite superior
        N (int): N pontos a serem sorteados

    Returns:
        tuple: Integral, incerteza estatística
    """
#    np.random.seed(1)
    x = np.random.uniform(a, b, N)
    Σfx = np.sum(f(x))
    integral = (b - a) * Σfx / N

    sigmaf = np.sqrt(1 / (N - 1) * (np.sum((f(x)) ** 2) - 1 / N * Σfx ** 2))
    sigmaI = (b - a) * sigmaf / np.sqrt(N)
    return integral, sigmaI
# Função que será integrada.
fx = lambda x: x**3

a = 0; b = 1 # Limites de integração.
N = 10_000
valor_exato = 0.25

print(f"\nIntegral de x^3 entre 0 e 1 pelo método da média com {N = }")
for i in range(0, 10):
    I, sigmaI = intMedia(fx, a, b, N)
    erro = abs(I - valor_exato)
    print(f"I = {I:.6f} | σI = {sigmaI:.6f} | erro absoluto = {erro:.6f}")


# Usando importance sampling

""" 
Para o importance sample é necessário realizar uma mudança de variável para 
tornar o integrando mais uniforme.

∫x^3dx, 0 -> 1. 

Dado p(x) = x^2

∫(x^3 / x^2) (x^2)dx,  g(y) = x e dy = x^2dx.

∫dy = ∫x^2dx ==> y = x^3/3 ==> x = (3y)^1/3 é o novo integrando.

Os novos limites ficam:
 0 <= x <= 1 ==> 0 <= y <= 1/3
 
∫(3y)^1/3dx, 0 -> 1/3 é a nova integral.

"""

fy = lambda y : (3 * y) ** (1/3) 

a = 0; b = 1/3

print("\nUsando o importance sample")
for i in range(0, 10):
    I, sigmaI = intMedia(fy, a, b, N)
    erro = abs(I - valor_exato)
    print(f"I = {I:.6f} | σI = {sigmaI:.6f} | erro absoluto = {erro:.6f}")