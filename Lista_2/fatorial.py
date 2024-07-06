# Calcula fatorial de um numero inteiro n não negativo

import sys

# Input do número.
n=int(input("Digite um número inteiro positivo "))

if n > 0:
    fatorial = 1
    # Loop que calcula o factorial.
    i = 1
    while i <= n:
        fatorial *= i
        i += 1
else:
    sys.exit("O número digitado não é inteiro positivo.")
# Exibe o resultado.
print(fatorial)


