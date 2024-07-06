""" 
Eu sou um lixo em probabilidade
"""


import numpy as np

verdes    = list(["verde" for i in range(0,41)])
vermelhas = list(["vermelha" for i in range(0,11)])
azuis     = list(["azul" for i in range(0,11)])
amarelas  = list(["amarela" for i in range(0,11)])
roxas     = list(["roxa" for i in range(0,11)])

todas_bolas = (verdes+vermelhas+azuis+amarelas+roxas)

N = 10**4
numero_de_eventos = 0
for i in range(0,N+1):
    sorteio = np.random.choice(todas_bolas,10)
    roxa = 0
    azul = 0 
    
    for i in sorteio:
        if i == "roxa":
            roxa+=1
        if i == "azul":
            azul+=1
        if azul == 2 and roxa == 2:
            numero_de_eventos += 1
print(numero_de_eventos / N)


