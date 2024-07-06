from math import sqrt, pi, cos, sin
import random
random.seed(5501)

def oneStep(x,y):
  z = random.uniform(0,1)
  if z > 0.75: 
      dx, dy = 0, 1 # Norte
  elif z > 0.50: 
      dx, dy = 0, -1 # Sul
  elif z > 0.25: 
      dx, dy = 1, 0 # Leste
  else: 
      dx, dy = -1, 0 #  Oeste
  x += dx 
  y += dy
  return x, y

def oneStep2(x,y):
  theta = random.uniform(0,1)*2*pi
  dx = cos(theta)
  dy = sin(theta)
  x += dx
  y += dy
  return x, y


Nexp = 1000
Npassos = 10
# Todas as caminhadas comecam da origem
x = [0]*Nexp
y = [0]*Nexp 
dist  = 0
dist2 = 0
dist_array = [0]*Nexp
for iexp in range(Nexp):
   for ipassos in range(Npassos):
      x[iexp], y[iexp] = oneStep2(x[iexp],y[iexp])
   d2 = x[iexp]**2 + y[iexp]**2
   dist += sqrt(d2)
   dist2 += d2
   dist_array[iexp] = sqrt(d2)
# Distancia media percorrida nos experimentos
media = dist/Nexp
rms = sqrt( dist2/(Nexp-1) - Nexp/(Nexp-1)*media**2 )
print("Passos: %d Experimentos: %d media = %f rms = %f" %(Npassos,Nexp,media,rms) )

#print(dist_array)
import numpy as np
print(np.mean(dist_array), np.std(dist_array,ddof=1))

#histograma
import matplotlib.pyplot as plt
#y1,bins1,c1=plt.hist(x,bins=int(sqrt(len(x))),color='firebrick',label='Data')
#y1,bins1,c1=plt.hist(dist_array,bins=int(sqrt(len(dist_array))),color='firebrick',label='Data')
y1,bins1,c1=plt.hist(dist_array,bins=20,color='firebrick',label='Data')
plt.ylabel('Ocorrências')
plt.xlabel('Distância média a partir da origem')

#plt.show()

#Fit
# Pesquisar um ajuste melhor e mais geral
import numpy as np
from scipy import random
from scipy.optimize import curve_fit
#def gauss(x): return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-1/2*((x-mean)/sigma)**2)
def func_fit(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2)) 

p0=[30,10,4.4]
#p0=[10,2.6,1.]
par=['norm','Mean','Std']
popt1, pcov1 = curve_fit(func_fit, bins1[1:], y1, p0)
pcov11=np.sqrt(np.diagonal(pcov1))
print(popt1, pcov1, pcov11)
xbins=np.linspace(-10,30,50)
#xbins=np.linspace(0,5,50)
plt.plot(xbins,func_fit(xbins,popt1[0],popt1[1],popt1[2]),c='navy',label='Fit')
#plt.legend(fontsize=15)
plt.show()

