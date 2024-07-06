# Calcula o seno de um angulo usando a série de Taylor com n = 5.

from math import sin, factorial


# função que calcula a série de taylor para o seno.
def seno(x,n):
    """
    Calcula o seno de um ângulo usando 
    a expansão de taylor.

    Args:
        x (float): ângulo
        n (int): número de somas

    Returns:
        float: seno do ângulo
    """
    soma = 0
    for n in range(0,n+1):
        soma += (((-1)**n) * (x**(2*n+1))) / factorial(2*n+1)
    return soma

# Ângulo do teste.
x = 1.2

# Número de somas.
n=5

# Chama a função seno e exibe o resultado.
resultado1 = seno(x,n)
print(f"O valor do algoritmo implementado para sen({x}) é {resultado1:.11f}")

# Resultado com a função sin do math.
resultado2 = sin(x)
print(f"O resultado com o módulo math é {resultado2:.11f}")




