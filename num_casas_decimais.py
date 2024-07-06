
"""
################################################################################
Existe o modulo 'uncertainties' para ajustar os algarismos
da incerteza.

Porém fiz esse codigo mesmo assim.
################################################################################
"""

numero = input("digite um número com zeros à esquerda: ")

#cria uma lista separando o ponto
b = numero.split(".")
print("\nAqui é retirado o ponto. ",b)

# cria uma lista com cada algarismo
lst = []
lst[:] = b[0]+ b[1]
print("Aqui é separado os algarismos. ",lst)

# conta quantos zeros a esquerda o num possui.
cont=0
for i in lst:
    i = float(i)
    if i != 0:
        break
    else:
        cont +=1

print("Quantidade de zeros à esquerda ",cont)

print(f"Esse é meu código mostrando apenas {float(numero):.{cont}f} de {numero}")

#===============================================================================
"""
A incerteza será exibida com 1 algarismo significativo.
Para mais algarismos, somar no contador.

EX: dois algarismos significativos

.{cont+1}f
"""

# exemplo usando o modulo.
import uncertainties
a = uncertainties.ufloat(0.02462631224438585, 3.350971888120506e-06)
print(f"\nEsse é um exemplo com o módulo (não é o número digitado). {a}")

# Diferentes formatações.
print(f'\nCom diferentes formatações: \n {a:.1u},\n {a:.3uf},\n {a:.2uL},\
    \n {a:0.2ue}')

#===============================================================================

