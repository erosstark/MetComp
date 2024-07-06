# Imprime os 10 primeiros números inteiros e suas raízes quadrada.

from math import sqrt

print("Número   sua raiz")
i = 0
while i < 10:
  r = sqrt(i)
  print(f"{i:3d} {r:11.2f}")
  i += 1



