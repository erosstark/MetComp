""" 
Eros Moreira Ferreira
17/04/2024 
Exibe alguns dados do arquivo que contem as medições da aceleração
da gravidade.

"""


import numpy as np 

# Guarda os dados do arquivo em uma array.
gravidade = np.loadtxt("C:/Users/eross/OneDrive/Documents/vscode python/MetComp/Lista_3/gravidade1.txt")

# conta quantas medidas foram realizadas.
num_medidas = 0
for i in gravidade:
    num_medidas += 1
    
# Calcula a média das medidas
soma = 0
for i in gravidade:
    soma += i 
media = soma/num_medidas

# Calcula o desvio padrão.
desv_padrao = np.sqrt((1/(num_medidas-1)) * sum([(x-media)**2 \
    for x in gravidade]))

# Percentual de medidas na media.
contador = 0
for x in gravidade:
    if  media - desv_padrao <= x <= media + desv_padrao:
        contador += 1
percentual = (contador/num_medidas) * 100

# Exibe os resultados e compara com o módulo numpy.
print(f" Os resultados para as medas da gravidade foram:\
\n programa  ||  módulo numpy")
print(f"{num_medidas:10d} {np.size(gravidade):10d} O número de medidas \
realizadas")
print(f"{media:10.1f} {np.mean(gravidade):10.1f} A médias das medidas(cm/s²)")
print(f"{desv_padrao:10.1f} {np.std(gravidade,ddof=1):10.1f} O desvio padrão(cm/s²)")
print(f"\n O percentual de medidas que está no intervalo\
 (media +- desvio padrao) é {percentual:.1f}%")


