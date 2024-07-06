"""
Eros Moreira Ferreira
12/06/2024
    Calcula a posição x e y do lançamento de um projetil
considerando a resistência do ar.
"""
import numpy as np
import matplotlib.pyplot as plt
def EDOs_Euler(f,S0,t0,tf,n):
    """

    Args:
        f (function): EDO que sera calculada. 
        S0 (array): condições iniciais.
        t0 (float): tempo inicial
        tf (float): tempo final 
        n (int): quantidade de passos 

    Returns:
        tuple: array[xi, vxi, yi, vyi], array[ti]
    """
    t = np.zeros(n+1)
    S = np.zeros((n+1,len(S0))) # S[i,k] solução equação k no tempo t[i]
    S[0] = S0
    t[0] = t0
    h = float(tf-t0)/n
    for i in range(n):
        t[i+1] = t[i] + h
        S[i+1] = S[i] + h * f(S[i], t[i])
    return  S, t


# EDO sem resistência do ar.
def EDO_projetil(S,t, B2m = 0):
    vx = S[1]
    vy = S[3]
    g  = 9.87
    return np.array([vx, -B2m*np.sqrt(vx**2 + vy**2)*vx, vy, \
        -B2m*np.sqrt(vx**2 + vy**2)*vy - g])


# EDO com resistência do ar.
def EDO_projetil_ar(S,t, B2m = 4*10**(-5)):
    vx = S[1]
    vy = S[3]
    g  = 9.87
    return np.array([vx, -B2m*np.sqrt(vx**2 + vy**2)*vx, vy, \
        -B2m*np.sqrt(vx**2 + vy**2)*vy - g])
    
# condições iniciais
x = 0; y = 0        # Posição inicial.
angulo = 45         # Ângulo de lançamento em graus.
v = 700             # Módulo da velocidade inicial.
vx = v*np.cos(np.radians(angulo))
vy = v*np.sin(np.radians(angulo))   # Componentes da velocidae.
s0 = np.array([x, vx, y, vy])
t0 = 0
n = 52
tf = 104

xi = EDOs_Euler(EDO_projetil,s0,t0,tf,n)[0]
xi_ar = EDOs_Euler(EDO_projetil_ar,s0,t0,tf,n)[0]

alcance_sem_ar = xi[:,0]
altura_sem_ar = xi[:,2]

alcance_ar = xi_ar[:,0]
altura_com_ar = xi_ar[:,2]

# Ângulo de alcance máximo.
angulo_max = 39
vx = v*np.cos(np.radians(angulo_max))
vy = v*np.sin(np.radians(angulo_max))
s0 = np.array([x, vx, y, vy])
xi_ar_max = EDOs_Euler(EDO_projetil_ar,s0,t0,tf,n)[0]

alcance_ar_max = xi_ar_max[:,0]
altura_ar_alcan_max = xi_ar_max[:,2]

""" 
Apliquei uma mascara y < 0, porém, como os passos são grandes (n é pequeno)
o gráfico não encostava no eixo x. Resolvi apenas cortar o eixo y < 0 no plot.
"""


plt.plot(alcance_sem_ar, altura_sem_ar,label = f"Sem resistência do ar {angulo}°")
plt.plot(alcance_ar, altura_com_ar, label = f"Com resistencia do ar {angulo}°")
plt.plot(alcance_ar_max, altura_ar_alcan_max, label = f"Com resistencia do ar {angulo_max}°")
plt.title(f"Lançamento de um projetil com e sem resistência do ar")
plt.xlabel("Distância(m)")
plt.ylabel("Altura(m)")
plt.legend(loc = "upper right")
plt.ylim(0,15000)
plt.axhline(color = "gray",zorder= 1)
plt.grid(True)
plt.savefig("projetil.pdf")
plt.show()


'''

"""
Achei mais interessante fazer uma função que testasse vários ângulos e retornasse o alcance maximo.
"""
#===============================================================================

# Acha o angulo em que o alcance é maxima
def alcanceXangulo(x0, y0, v0, EDO, t_step_EDO = 100, t_step = 0.1, max_data = False, max_only = False):
    """
    Cálcula o alcance máximo de um projétil em função de ãngulo de lançamento.

    Args:
        EDO (fun): EDO projetil
        x0 (float): coordenada x inicial
        y0 (float): coordenada y inicial
        v0 (float): módulo da velocidade inicial
        t_step_EDO (int):    numero de passos da EDO
        t_step (float, optional): incremento no tempo máximo tf da EDO.
        Defaults to 0.1.
        max_data (bool, optional): Retorna o alcance máximo, ângulo e tempo do
        alcance máximo. Defaults to False.
        max_only (bool, optional): Retorna apenas o alcance máximo. Defaults to False.

    Returns:
        tuple: alcances maximo, angulos, tempos do alcance maximo
    """
    alcances = []
    angulos = []
    tempos = []

    for i in range(10,90): # angulos de 10° a 89°
        vx = v0*np.cos(np.radians(i))
        vy = v0*np.sin(np.radians(i))
        s0 = np.array([x0, vx, y0, vy])
        t0 = 0
        tf = 1
        xi = EDOs_Euler(EDO,s0,t0,tf,n)[0]
        while xi [-1,2] > 0:   # verifica se  altura é maior que zero
            tf = tf + t_step
            xi = EDOs_Euler(EDO,s0,t0,tf,t_step_EDO)[0]
        tempos.append(tf)
        alcances.append(xi [-1,0])
        angulos.append(i)
    index_max = alcances.index(max(alcances))
    if max_only:
        return alcances[index_max]
    elif max_data:
        return alcances[index_max], angulos[index_max], tempos[index_max]
    else:
        return alcances, angulos, tempos
    
alcance_max = alcanceXangulo(x, y, v, EDO_projetil_ar, n, max_data=True, t_step =1)
print(f"O alcance maximo é {alcance_max[0]} m, no angulo {alcance_max[1]}° e o tempo do alcance é {alcance_max[2]} s")

alcances_ar, angulos_ar, tempos_ar = alcanceXangulo(x, y, v, EDO_projetil_ar, \
    n, t_step = 1)

alcances, angulos, tempos = alcanceXangulo(x, y, v, EDO_projetil, n, t_step = 1)

plt.plot(angulos, alcances, label = "Sem resistência do ar")
plt.plot(angulos_ar, alcances_ar, label = "Com resistência do ar")
plt.title("Alcance X angulo de disparo")
plt.xlabel("angulo(°)")
plt.ylabel("Alcance(m)")
plt.legend(loc = "upper right")
plt.grid(True)
plt.show()

#===============================================================================

'''