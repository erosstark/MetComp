"""
Eros Moreira Ferreira
26/06/2024

metodo da rejeição de seno
"""
import numpy as np
import matplotlib.pyplot as plt

k = np.pi/2
a = 0.785398
func_pdf = lambda y:a * np.sin(k*y)

sement = np.random.seed(int(input("Digite o semente: ")))
N = int(input("Digite o numero de eventos: "))

# método da rejeição
def rejeicao(N, z):
    numeros_aceitos = []
    while len(numeros_aceitos) < N:
        y = np.random.uniform(0, 2)
        u = np.random.uniform(0, z)
        numeros_aceitos.append(y) if u < func_pdf(y) else None
    return numeros_aceitos

eventos = rejeicao(N,a)
media2 = np.mean(eventos)
desv_padrao2 = np.std(eventos, ddof = 1)



# histrograma dos eventos
plt.hist(eventos, bins=100, density=True)
# plot da função pdf 
plt.plot(np.linspace(0, 2, 100), func_pdf(np.linspace(0, 2, 100)))

plt.xlabel('y')
plt.ylabel('Densidade')
plt.text(1.7,0.7,f"$\mu$ = {media2:.2f}\n$\sigma$ = {desv_padrao2:.2f}")
plt.title('Distribuição gerada pelo método da rejeição da PDF $f(y) = asin(ky)$')
plt.savefig("rejeição_seno.pdf")
plt.show()

""" 
foi usado o número 2 para a semente e 100000 para o numero de eventos.
"""