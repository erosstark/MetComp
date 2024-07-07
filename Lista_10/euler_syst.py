import numpy as np

def Euler(f,S0,t0,tf,n):
    t = np.zeros(n+1)
    if isinstance(S0, (float, int)):  #True if S0 is a list of floats or ints
        S = np.zeros(n+1)  # S[k] is the solution at time t[k]
    else:
        S = np.zeros((n+1,len(S0)))
    S[0] = S0
    t[0] = t0
    h = float(tf-t0)/n
    for i in range(n):
        t[i+1] = t[i] + h
        S[i+1] = S[i] + h * f(S[i], t[i])
    return  S, t