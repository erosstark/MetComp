# dois dados
import numpy as np
N=10**6
dado = np.random.randint(1,7,N)
contador = 0
for i in range(0,N):
    if dado[i] > 4:
        contador +=1

print(contador/N)

""" 
O exercicio pede >= 4 e fala que o resultado deve ser 0.3,
que só ocorre se for >4. Exercicio esta errado.
"""
