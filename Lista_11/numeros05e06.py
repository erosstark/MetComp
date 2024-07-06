# probabilidade de numeros entre 0.5 e 0.6

import numpy as np
np.random.seed(1)
numeros = np.random.random(size=100000)
contador = 0
for i in numeros:
    if 0.5 < i < 0.6:
        contador+=1

P = contador/np.size(numeros)
print(P)

