""" 
Eros Moreira Ferreira
24/04/2024

Calcula as raízes de uma equação de segundo grau.
"""

from numpy.lib.scimath import sqrt

def roots(a,b,c):
    """
    Calcula as raizes de uma equação de 
    segundo grau ax^2 + bx + c = 0 
    dados seus coeficientes a, b e c.

    Args:
        a, b, c (float): coeficientes.

    Returns:
        tuple: raízes x1 e x2
    """
    delta = (b**2) - 4 * c * a
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    return x1, x2

# Input dos coeficientes da equação.
a =float(input(" ax² + bx + c = 0 , a = "))
b =float(input(f" {a}x² + bx + c = 0 , b = "))
c =float(input(f" {a}x² + {b}x + c = 0 , c = "))

# Raízes.
x1, x2 = roots(a,b,c)


print(f"As raizes da equação {a}x² + {b}x + {c} = 0")
print(f"{x1 = :.2f} e {x2 = :.2f}")
print(f"{type(x1) = } {type(x1) = }")

""" 
Dúvidas em relação ao comando do exercício 
' Se ∆ > 0, o resultado deve ser do tipo float. 
Se ∆ < 0 o resultado deve ser do tipo
complex'

É para a função roots retornar complex ou float? 
A função retorna uma tuple com elementos numpy.complex128 ou numpy.float64.
É para converter para complex ou float?
"""
