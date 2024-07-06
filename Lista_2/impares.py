# dado um número inteiro positivo n, 
# imprime os n números primeiros ímpares e sua soma.

import sys

# Input do número.
n = int(input("Digite um número inteiro positivo "))

if n > 0: #Verifica se a entrada é válida.
    soma = 0
    impares = 1
    print(f"Os {n} primeiros naturais ímpares são")
    # Loop que calcula os n primeiros impáres e sua soma.
    k = 1
    while k <= n:
        print(impares)
        soma += impares
        impares += 2
        k += 1
else:
    sys.exit("O número precisa ser inteiro positivo.")

# Exibe o resultado final.
print(f" A soma dos {n} primeiros ímpares é {soma}.\n Uma observação\
 interessante é que a soma dos n primeiros ímpares é n^2")





