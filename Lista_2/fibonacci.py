#  Exibe os primeiros 100 números da série de Fibonacci.

# Defini os primeiros 2 digitos.
i = 1
j = 1

# Loop que calcula os outros 98 digitos.
contador = 2
print(f"Os 100 primeiros números da série de fibonacci são:\n{i} \n{j}")
print(f"contador ----|---- Número Fibonacci")
while contador < 100:
  m = i
  n_fibonacci = i + j
  i = j
  j = m + j
  contador += 1
  print(f"{contador:3d} {n_fibonacci:30d}")



