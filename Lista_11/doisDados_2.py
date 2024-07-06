# dois dados (verde e preto)
import numpy as np
N=1000000
dado_verde = np.random.randint(1,7,N)
dado_preto = np.random.randint(1,7,N)

contador = 0
for i in range(0,N):
    if dado_preto[i] > dado_verde[i]:
        contador +=1

print(f"{contador/N:.2f}")
