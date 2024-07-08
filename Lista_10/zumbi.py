""" 
Eros Moreira Ferreira

Podemos modelar o ataque de zumbis a uma populac¸ao de humanos através
da soluc¸ao do seguinte sistema de equacões diferenciais:

dS/dt = Σ - βSZ - δsS
dI/dt = βSZ - ρI - δiI
dZ/dt = ρI - αSZ
dR/dt = δsS + δiI + αSZ

Nestas equações S, I, Z e R representam quatro categorias:
    Os humanos suscetíveis a se tornarem zumbis (S)
    Os humanos infectados mordidos por zumbis (I)
    Os zumbis (Z)
    Os removidos (R) ( zumbis presos ou humanos mortos)
    
S(t), I(t), Z(t) e R(t) sao os números de indivíduos em cada categoria ao
longo do tempo. A unidade de tempo e a hora.

Os parametros representam: 
    Σ Numero de novos humanos levados para a área infectada por unidade
de tempo
    β probabilidade de um encontro de um humano com um zumbi, por
unidade de tempo, resultando em um infectado
    α probabilidade de que um humano mate um zumbi, por unidade de
tempo
    δs probabilidade de que um humano suscetível morra, por unidade de
tempo
    δi probabilidade de que um humano infectado morra, por unidade de
tempo
    ρ probabilidade de que um humano infectado se torne zumbi, por
unidade de tempo

Para ser mais fiel ao filme, podemos definir 3 fases, cada uma com um
conjunto de valores de parametros: 
    fase 1 - as primeiras 4 horas: humanos se encontram com um zumbi:
Σ = 20, β = 0.03, ρ = 1, δs = 0, δi = 0, α = 0
    fase 2 - duração de 24 horas: a praga de zumbis se torna evidente: 
Σ = 2, β = 0.0012, ρ = 1, δs = 0, δi = 0.014, α = 0.0016
    fase 3 - apos as primeiras 28 horas: contra-ataque dos humanos: 
Σ = 2, β = 0 (humanos nao são mais infectados), ρ = 1, δs = 0.0067, δi = 0.014, α = 0.006


"""

import numpy as np
import matplotlib.pyplot as plt
from euler_syst import Euler
from rk4 import RungeKutta4

fase1 : dict = {'Σ' : 20, 'β': 0.03, 'ρ': 1, 'δs': 0, 'δi': 0, 'α': 0}
fase2 : dict = {'Σ' : 2, 'β': 0.0012, 'ρ': 1, 'δs': 0, 'δi': 0.014, 'α': 0.0016}
fase3 : dict = {'Σ' : 2, 'β': 0, 'ρ': 1, 'δs': 0.0067, 'δi': 0.014, 'α': 0.006}

def zumbi(t, S, I, Z, R):
    return np.array([Σ - βSZ - δsS, βSZ - ρI - δiI, ρI - αSZ, δsS + δiI + αSZ])

