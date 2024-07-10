""" 
Eros Moreira Ferreira
08/04/2024

Calcula uma aproximação para a função sen(x) para x = pi/6 e 3pi/4 usando a série de taylor com 
n = 3, 5 e 7.

"""

import numpy as np
from math import factorial
import matplotlib.pyplot as plt

def taylor_seno(x:float,N:int):
    """
    Calcula a função seno usando a serie de taylor

    Args:
        x (float): angulo em radiano 
        N (int): termo máximo da série

    Returns:
        float:senx
    """
    senx = [((-1) ** n) * (x **(2 * n + 1)) / factorial(2 * n + 1)\
        for n in range(0,(N//2)+1)]
        
    return sum(senx)



# Para x = pi/6 e 3pi/4.
Ns = [3,5,7]
xs = [np.pi/6, 3*np.pi/4]
xstr = ["pi/6","3pi/4"]        # Texto para ser exibido.

i = 0                          # index da lista do texto a ser exibido.
for x in xs:
    for N in Ns:

        # Aproximação usando a série de Taylor.
        sin_aprox = taylor_seno(x,N)
        print(f"{N = }  x = {xstr[i]} \nValor aproximado do seno({xstr[i]}) é: {sin_aprox}")

        # Diferença entre a aproximação e o valor obtido com np.sin(x).
        print(f"Diferença entre a aproximação e np.sin({xstr[i]}) = {abs(np.sin(x) - sin_aprox)} ")

        # Proximo termo da série.
        prox_termo = taylor_seno(x,N+2) - taylor_seno(x,N)
        print(f"Valor do próximo termo da série : {prox_termo} \n ")

    i += 1



# Valores de x para plotar o gráfico

x = np.linspace(0, 3*np.pi/2, 51)

# Gráfico np.sin(x)
plt.plot(x, np.sin(x),"r")

# Gráfico N=3
N=3
y3 = taylor_seno(x,N)
plt.plot(x,y3,"g")

# Gráfico N=5
N=5
y5 = taylor_seno(x,N)
plt.plot(x,y5)

# Gráfico N=7
N=7
y7 = taylor_seno(x,N)
plt.plot(x,y7,"b")


# Gráfico N=9
N=9
y9 = taylor_seno(x,N)
plt.plot(x,y9,"y")


# Formatação do gráfico
plt.ylim(top = 2, bottom = -2)
plt.xticks(np.linspace(0, 25*np.pi/18, 6),['0','50','100','150','200','250'])
plt.title("Série de Taylor - Sen(x)")
plt.xlabel("x(graus)")
plt.ylabel("Sen(x)")
plt.legend(["Sen(x)","N=3" , "N=5", "N=7","N=9"])
plt.grid(True)

plt.savefig("seno.png")
plt.show()


