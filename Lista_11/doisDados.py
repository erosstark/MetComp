# dois dados
import numpy as np
N = 10**6
dado1 = np.random.randint(1,7,N)
dado2 = np.random.randint(1,7,N)

contador = 0

for i in range(0,N):
    if dado1[i] == 6 and dado2[i] == 6:
        contador +=1

print(f" Resultado: {contador/N:.3f}")

print(f" Resultado esperado: {1/36:.3f}")