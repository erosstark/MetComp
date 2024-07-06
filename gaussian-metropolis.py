#Gera numeros distribuidos de acordo com Gaussiana usando Metropolis
import random
import numpy as np
import matplotlib.pyplot as plt

def wMet(x): return np.exp(-0.5*x*x) 

def randMet(xrnd, w, delta):
#----------------------------------------------------------------------------
 #  Generates random numbers xrnd with the distribution w(x) by the Metropolis
 #  method, using a maximal trial step size delta
#----------------------------------------------------------------------------    
    dx = delta * random.uniform(-1,1) # trial step size
    w = w(xrnd+dx)/w(xrnd)
    if w>= 1 : xrnd += dx
    elif (random.uniform(0,1) <= w ) : xrnd += dx   # accept with prob. w(x) 
    return xrnd
 
random.seed(5501)
Nexp = 1000000
x_array = [0]*Nexp                 
#randMet(wMet,0.1e0,0) #inicializa RNG
x_array[0] = random.uniform(-1,1) 
print (0, x_array[0])
for iexp in range(0,Nexp-1): 
    x_array[iexp+1]=randMet(x_array[iexp], wMet, 0.5)
    #print (iexp, x_array[iexp+1] ) 

#histograma
y1,bins1,_=plt.hist(x_array,bins=50,color='green',label='Data', range=(-4,4))
#fit
from scipy.optimize import curve_fit
def func_fit(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))
p0=[30,0,1]
par=['norm','Mean','Std']
popt1, pcov1 = curve_fit(func_fit, bins1[1:], y1, p0)
xbins=np.linspace(-4,4,50)
plt.plot(xbins,func_fit(xbins,popt1[0],popt1[1],popt1[2]),c='navy',label='Fit')



plt.show()
  


