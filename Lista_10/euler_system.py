"""Função que implementa método de Euler para um sistema de ODEs acopladas"""
import numpy as np
def Euler(f, S0, ti, tf, n):
    """Metodo de Euler pra x'= f(x,t), x(0) = xi,
       com n passos de ti até tf"""
    t = np.zeros(n+1)   # n+1 para incluir o ultimo instante tf
    if isinstance(S0, (float, int)):  #True if S0 is a list of floats or ints
        S = np.zeros(n+1)  # S[k] is the solution at time t[k]
    else:
        S = np.zeros((n+1,len(S0)))

    S[0] = S0
    t[0] = ti 
    h = float(tf-ti)/n
    for k in range(n):
        #print (t[k], S[k], np.tan(t[k]),f(S[k], t[k]) )
        t[k+1] = t[k] + h
        S[k+1] = S[k] + h*f(S[k], t[k])
    return S, t

def f(S,t):
    v0x = 5.; v0y = 10.;  ax = 2.
    return np.array([v0x-ax*t , v0y-S[0]*t ])

ti=0.
tf=4.
S0 = np.array([0.,15.])
n=200

S1, t1 = Euler(f, S0, ti, tf, n)
#print(S1,t1)


import matplotlib.pyplot as plt
plt.figure()
plt.plot(t1, S1[:,0], 'r')
plt.xlabel('t')
plt.ylabel('x')
plt.title("x(t)")
#plt.savefig('euler_gaus.png')

plt.figure()
plt.plot(t1, S1[:,1], 'r.')
plt.xlabel('t')
plt.ylabel('y')
plt.title("y(t)")
#plt.savefig('euler_gaus.png')

plt.figure()
plt.plot(S1[:,0], S1[:,1], 'r.')
plt.xlabel('x')
plt.ylabel('y')
plt.title("y(x)")
#plt.savefig('euler_gaus.png')

plt.show()





