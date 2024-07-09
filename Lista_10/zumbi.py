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


# Função zumbi
def zumbi(s,t, params):
    Σ = params[0]['Σ']
    β = params[0]['β']
    ρ = params[0]['ρ']
    δs = params[0]['δs']
    δi = params[0]['δi']
    α = params[0]['α']
    S = s[0];  Z = s[1]; I = s[2]; R = s[3]
    
    return np.array([Σ - β*S*Z - δs*S, ρ*I - α*S*Z, β*S*Z - ρ*I - δi*I, δs*S + δi*I + α*S*Z])
    
    
# Paarâmetros de cada fase.
fase1 : dict = {'Σ' : 20, 'β': 0.03, 'ρ': 1, 'δs': 0, 'δi': 0, 'α': 0}
fase2 : dict = {'Σ' : 2, 'β': 0.0012, 'ρ': 1, 'δs': 0, 'δi': 0.014, 'α': 0.0016}
fase3 : dict = {'Σ' : 2, 'β': 0, 'ρ': 1, 'δs': 0.0067, 'δi': 0.014, 'α': 0.006}



# Condições iniciais. S0 = ( S, Z, I, R )
S0 = [60, 1, 0, 0]   
                    #[i , f] em horas
timeSpan = np.array([[0, 4],\
                     [4, 28],\
                     [28, 60]]) # fase 1,\ fase 2,\ fase 3
dt = 0.05 # passo de tempo


# Solução pelo metodo de Euler
for fase, i in zip([fase1, fase2, fase3], range(0,3)):
   sol, t = Euler(zumbi, S0, timeSpan[i,0], timeSpan[i,1], fase, TimeStep=dt)
   S0 = sol[-1,:] # Atualiza o as condiçoes iniciais de cada fase

   # Plota os resultados
   humanos, = plt.plot(t, sol[:,0], 'r')
   zumbis, = plt.plot(t, sol[:,1], 'g')
   infectados, = plt.plot(t, sol[:,2], 'b')
   removidsos, = plt.plot(t, sol[:,3], 'y')

plt.axvspan(0, 4, color = "green", alpha = 0.1)  # Pinta as regiões de cada fase
plt.axvspan(4, 28, color = "pink", alpha = 0.1)
plt.axvspan(28, 60, color = "yellow", alpha = 0.1)
plt.legend([humanos, zumbis, infectados, removidsos], ["Humanos suscetíveis (S)", "Zumbis(Z)",\
    "Humanos infectados(I)", "Removidos(R)"])
plt.xlabel("Tempo (horas)")
plt.ylabel("Idinvíduos")
plt.title("Noite dos Mortos Vivos")

plt.show()


