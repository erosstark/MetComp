"""
Eros Moreira Ferreira
30/05/2024
Calcula a integral usando o método de Simpson de uma função
"""
import numpy as np
import scipy.integrate as integrate


#================================================================
def Trapezio(fun,a,b,k):
    """
        Calcula a integral de uma função
    usando o método dos trapézios.

    Variáveis:
        fun - função a ser integrada.
        a, b - limites de integração.
        k - índice.

        Retorna a integral aproximada por
    2^k trapézios.

    """
    global contador
    contador += 1
    delx = (b-a) / 2**k
    fj = 0
    for j in range(1,2**k):
        fj += fun(a + j*delx)
    t = (delx/2) * (fun(a) + fun(b) + 2*fj)
    return t
#================================================================

# Função para ser integrada.
f = lambda x: x**2 * np.exp( (-3 * x**2) / 2)
# Fator de normalização
N = 4 * np.pi * (3 / (2*np.pi))**(3 / 2)

# Limites de integração.
a, b =0, 2

# Número máximo de iteração e precisão.
intmax = 20
erro = 1e-6

# Valor da integral usando scipy.integrate.
I = integrate.quad(f, a, b)
I = I[0]
# Loop que chama a função simpson e vérifica se a precisão desejada foi alcançada.
print(f"O valor esperada para a integral de acordo com scipy é {I:.10e}. \n\
Aproximando com o método de Simpson até a precisão relativa {erro} temos:\n")

print(" k   Aproximação            Diferença relativa para o valor esperado")
contador = 0
s_anterior = 10**16
k = 1
tk_anterior = 10**16
while k < intmax:
    tk = Trapezio(f,a,b,k)
    s = tk + (tk - tk_anterior) / 3
    tk_anterior = tk
    print(f"{k:2d} | {s:.10e}    |  {abs(I - s)/I:.10e}")

    # Verifica a precisão.
    if abs((s - s_anterior) / s) < erro:
        break
    else:
        s_anterior = s
        k += 1
print(f"A função foi chamada {contador} vezes")

print(f"R = {N * s} com o método de Simpson")
print(f"R = {N * I} com a integral scipy")



