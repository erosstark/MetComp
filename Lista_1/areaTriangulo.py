# Calcula a área de um triângulo dados o comprimento de seus lados.

from math import sqrt
import sys

print("Para calcular a área de um triângulo, digite o comprimento de seus lados")
# Requisita o comprimento dos lados do triângulo
s1, s2, s3 = float(input("Comprimento lado 1: ")), float(input("Comprimento lado 2: ")), float(input("Comprimento lado 3: "))

# Verifica a condição de existência do triângulo.
if (s1 - s2) < s3 < (s1 + s2) and \
    (s2 - s3) < s1 < (s2 + s3) and \
        (s1 - s3) < s2 <(s1 + s3):
    # Calcula a área
    s = (s1 + s2 + s3) / 2
    area = sqrt(s * (s-s1) * (s-s2) * (s-s3))
else:
    sys.exit("Esse Triângulo não existe.")

print(f"A área do triângulo de lados {s1}un, {s2}un e {s3}un é {area:.2f}un^2")




