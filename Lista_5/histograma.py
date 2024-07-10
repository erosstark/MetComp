""" 
Eros Moreira Ferreira
08/05/2024

Gera um histograma de uma lista de dados de medidas da gravidade.
"""

import numpy as np
import matplotlib.pyplot as plt

gravidade = np.loadtxt("gravidade.txt")

media = np.mean(gravidade)
desv_padrao = np.std(gravidade, ddof = 1)

for n_bins in [20,60]:
    plt.hist(gravidade, bins = n_bins, density = True, edgecolor = "b")

    plt.figtext(0.14, 0.77, f"Valor médio $\sigma$={media:.2f}cm/$s^2$ \
\nDesvio padrao $\mu$={desv_padrao:.2f}",backgroundcolor = (0, 0.5, 1, 0.5))
    plt.show()




