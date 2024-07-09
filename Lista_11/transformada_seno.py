"""
Eros Moreira Ferreira
26/06/2024

Transformada de seno
"""
import numpy as np
import matplotlib.pyplot as plt

k = np.pi/2
a = 0.785398
func_pdf = lambda y:a * np.sin(k*y)
invert_cdf = lambda x:  np.arccos(1-k*x/a)/k

sement = np.random.seed(int(input("Digite o semente: ")))
N = int(input("Digite o numero de eventos: "))

# Método da transformada.
amostra_uniforme = np.random.uniform(0,2*a/k,N)
amostra = [invert_cdf(i) for i in amostra_uniforme]

media1 = np.mean(amostra)
desv_padrao1 = np.std(amostra, ddof = 1)

# Histrograma da eventos
plt.hist(amostra, bins = 100, density=True)
# plot da função pdf
plt.plot(np.linspace(0, 2, 100),func_pdf(np.linspace(0, 2, 100)))

plt.ylabel("Densidade")
plt.xlabel('y')
plt.text(1.7,0.7,f"$\mu$ = {media1:.2f}\n$\sigma$ = {desv_padrao1:.2f}")
plt.title("Distribuição gerada pela método da transformada da PDF $f(y) = asin(ky)$")
#plt.savefig("transformada_seno.pdf")
plt.show()

""" 
foi usado o número 2 para a semente e 100000 para o numero de eventos.
"""