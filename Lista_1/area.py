# Calcula a área de de um retângulo e sua incerteza dado as
# medidas dos seus lados e suas incertezas.

from uncertainties import ufloat
from math import sqrt


# Input das medidas dos lados e suas incertezas
a, inc_a = float(input("Medida do lado a: ")), float(input("Incerteza do lado a: "))
b, inc_b = float(input("Medida do lado b: ")), float(input("Incerteza do lado b: "))

# Calculo da área e incerteza.
area = a * b
inc_area = sqrt( ((inc_a / a)**2) + ((inc_b / b)**2) ) * area

# Usando modulo uncertainties para exibir a quantidade de algarismos corretos.
resultado = ufloat(area,inc_area)

print(f"A área do retângulo é {resultado:.1u}")