import numpy as np

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