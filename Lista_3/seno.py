""" 
Eros Moreira Ferreira
17/04/2024 
Calcula o seno de um angulo usando a série de Taylor com n = 2.

"""

from math import factorial

# Ângulo do teste.
x = 1.2

# Número de somas.
n=2

# Calcula o somatório 
senx = sum( [ (((-1)**n) * (x**(2*n+1))) / factorial(2*n+1) 
            for n in range(0,n+1) ] )

# Exibe o resultado ao final da soma.
print(f"Sen(x) para x = 1.2 é {senx:.6f}")


"""
Usando sen(x) do módulo math,
para x = 1.2, sen(x) = 0.932039,
já no algorítmo acima, sen(x) = 0.932736.
"""


