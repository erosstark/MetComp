import numpy as np

def Euler(f,S0,t0,tf,n, *args):
    """
    Calcula a solução para um sistema de EDOs de primeira ordem
    pelo método de Euler	

    Args:
        f (func): função do sistema de EDOs
        S0 (int, float or list): Condições iniciais
        t0 (_type_): tempo inicial
        tf (_type_): tempo final
        n (_type_): número de iterações

    Returns:
        tuple: _solução do sistema de EDOs, tempo 
    """
    t = np.zeros(n+1)
    if isinstance(S0, (float, int)):  #True if S0 is a list of floats or ints
        S = np.zeros(n+1)  # S[k] is the solution at time t[k]
    else:
        S = np.zeros((n+1,len(S0)))
    S[0] = S0
    t[0] = t0
    h = float(tf-t0)/n
    
    if args:
        for i in range(n):
            t[i+1] = t[i] + h
            S[i+1] = S[i] + h * f(S[i], t[i], args)
    else:
        for i in range(n):
            t[i+1] = t[i] + h
            S[i+1] = S[i] + h * f(S[i], t[i])
            
    return  S, t