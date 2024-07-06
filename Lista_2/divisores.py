# Calcula todos os divisores de um dado número n 
# inteiro positivo e a quantidade.

import sys

# Input do número.
n = int(input("Digite um número inteiro positivo "))

if n > 0: # Verifica se o número é válido.
    numero_divisores = 0
    print ("Divisores:")
    # loop que calcula os divisores.
    i = 1
    while i <= n:
        if n % i == 0:
            print("%6d" % i)
            numero_divisores += 1
            i += 1
        else:
            i += 1
else:
    sys.exit("Precisa ser um número inteiro positivo.")
    
print(f"Total de divisores: {numero_divisores}")






