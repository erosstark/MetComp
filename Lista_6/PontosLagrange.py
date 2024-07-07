"""
Eros Moreira Ferreira

Calcula a distância r do ponto L1 ao Sol.


O método de NR não retornou um valor satisfatório. A bisseção foi a solução melhor.
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
#%%
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
#%%
#%%
def NR_raiz(f, df, x0, precisao = 1e-7, limite = 100):
    """
    Calcula a raíz de uma função usando o método de Newton-Raphson.

    Precisao de 10^(-7) casas decimais e o limite máximo
  de iterações e 100.

    A partir de um ponto x0 fornecido, converge para a raíz mais
  próxima desse ponto. O ponto fornecido nao pode zerar a derivada.

    O metodo de Newton Raphson pode resolver casos em que o
  metodo da bisseção falha.
  
  CONSIDERAÇÕES:
    As vezes pode não convergir para a raíz desejada.
    É importante que o ponto esteja próximo da raíz desejada.
    Nem sempre converge!

    Args:
        f (func): função que terá raiz encontrada
        df (func): derivada da função acima
        x0 (float): chute inicial
        precisao (float, optional): precisão absoluta. Defaults to 1e-7.
        limite (int, optional): limite máximo de interações. Defaults to 100.

    Returns:
        tuple: raíz e o número de iterações
    """
    nit = 0
    x = x0 - f(x0) / df(x0)

    # Loop que calcula a raíz.
    while  abs(x-x0) > precisao and nit < limite:
        x0 = x
        x = x0 - f(x0) / df(x0)
        nit += 1
    return x0, nit

#%%


# Constantes utilizadas
R = 1.5e11 # Distância entre a terra e o sol (m)
m = 5.9736e24 # Massa da terra (kg)
M = 1.989e30 # Massa do Sol (kg)
w = 1.992e-7 # Velocidade angular da Terra e do satélite (1/s)
G = 6.674e-11 # Constante de gravidade (m^3 kg^-1 s^-2)

def EqDistancia(r):
    """
    Função cuja raiz é a distância entre L1 e o Sol.
    """
    return G * M / r**2 - G * m / (R - r)**2 - w**2 * r

def Derivada_EqDistancia(r):
    """
    Derivada da EqDistancia em relação a x.
    """
    return -2 * G * M / r**3 + 2 * G * m / (R - r)**2 - w**2

#%%
# Plotando a EqDistancia
x = np.linspace(1.40e11, 1.49e11, 90000)
y = EqDistancia(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# De acordo com o gráfico, a raiz da EqDistancia está entre 1.48e11 e 1.50e11.

#%%
# Calculando a raíz da EqDistancia

print(NR_raiz(EqDistancia,Derivada_EqDistancia, 1.49e11, precisao = 1e1))
# %%
raiz_bissecao = bissecao(EqDistancia, 1.48e11, 1.49e11, precisao = 1e1)
# %%

# Valor da primeira iteração de NR_raiz
x = 1.48e11 - EqDistancia(1.48e11) / Derivada_EqDistancia(1.48e11)
print(x)
print(abs(x - 1.48e11))
print(raiz_bissecao) # valor mais próximo da raiz.
# %%
