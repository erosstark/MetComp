""" 
Eros Moreira Ferreira
15/04/2024

Calcula a intercesão das duas funções usando o método da bisseção
"""
import matplotlib.pyplot as plt
import numpy as np

# funçoes P(x) e Q(x)
P = lambda x: x*np.tan(x)
Q = lambda x: np.sqrt(16 - x**2)

# Gráfico
x = np.linspace(0, 4, 1000)
y = P(x)
ym = np.ma.MaskedArray(y, np.abs(y)>20)
z = Q(x)

plt.plot(x, ym, label = r"P(x) = $xtang(x)$")
plt.plot(x, z, label = r"Q(x) = $\sqrt{16-x^2}$")
plt.ylim(-2,20)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend(loc = "upper right")
#plt.savefig("bissecao.pdf")
plt.show()


def bissecao(f, xmax, xmin, precisao = 1e-7, intmax = 100):
    """
    Calcula uma aproximação para a raiz de um polinômio no intervalo [xmin, xmax]
    LIMITAÇÕES!!!
    O método não serve para:
      intervalos que possuem mais de uma raiz.
      Intervalos com singularidade.
      Raiz que não cruza o eixo x.
      funções descontínuas no invertvalo [xmin, xmax].

    Args:
        f (function): polinômio
        xmax (float): 
        xmin (float): 
        precisao (float, optional): . Defaults to 1e-7.
        intmax (int, optional): número máximo de interações. Defaults to 100.

    Returns:
        tuple: raiz, interaçoes
    """
    nit = 0
    fmin = f(xmin)
    if f(xmax) * fmin > 0:
        return print("intervalo inadequado")
    else:
        while abs(xmax-xmin) > precisao and nit < intmax:
            xmedio = (xmax+xmin) / 2
            fmedio = f(xmedio)
            if fmin * fmedio < 0:
                xmax = xmedio
            else:
                xmin = xmedio
            nit += 1
        return xmedio, nit

# 0 = P(x) - Q(x)
f = lambda x: x*np.tan(x) - np.sqrt(16 - x**2)

raiz1 = bissecao(f,1, 1.5,precisao=1e-5)
raiz2 = bissecao(f,3.5, 4,precisao=1e-5)

print(f"A intersecção das duas funções ocorre em x1 = {raiz1[0]:.5f} e \
 x2 = {raiz2[0]:.5f} com {raiz1[1]} e {raiz2[1]} iteracões, respectivamente.")



