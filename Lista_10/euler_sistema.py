
import numpy as np
import matplotlib.pyplot as plt

def EDOs(f,S0,t0,tf,n):
    t = np.zeros(n+1)
    S = np.zeros((n+1,len(S0))) # S[i,k] solução equação k no tempo t[i]
    S[0] = S0
    t[0] = t0
    h = float(tf-t0)/n
    for i in range(n):
        t[i+1] = t[i] + h
        S[i+1] = S[i] + h * f(S[i], t[i])
    return  S, t

# edo para ser calculada 
def f(S,t):
    v0x = 5; v0y = 10; ax = 2
    return np.array([v0x - ax * t, v0y - S[0] * t])

# variáveis.
s0 = np.array([0,15])
ti = 0
tf = 4
n = 10

xi ,ti = EDOs(f,s0,ti,tf,n)

plt.plot(ti, xi[:,1])
plt.show()