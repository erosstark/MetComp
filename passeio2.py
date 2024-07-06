import numpy as np
from math import sqrt
import random
import turtle  # https://docs.python.org/3/library/turtle.html

random.seed(5500)

Nexp = 500 # Numero de experimentos (de bebados...)
NpassosMax = 100 # Numero maximo de passos em cada experimento
step = 20

Nshow = 50  # Numero de experimentos a serem mostrados na animacao

color = ["Aqua","Azure", "BlueViolet", "DarkGreen", "DarkMagenta", "DarkOrange", "DarkRed", "DarkViolet", "DeepPink", "FireBrick", "ForestGreen", "Indigo", "LightGoldenRodYellow" ]

wn = turtle.Screen()
wn.bgcolor("light green")
man = []
for iexp in range(Nshow): 
   t = turtle.Turtle()
   t.speed(8)  # Speeds from 1 to 10 enforce increasingly faster animation of line drawing and turtle turning. speed = 0 means that no animation
   t.shape("turtle")
   t.shapesize(0.5,0.5,0)
   t.color(random.choice(color))
   man.append(t)

# Just mark the origin
t = turtle.Turtle()
t.dot(20)

x = [0]*Nexp # Todos comecam da origem
y = [0]*Nexp

# Defina se as caminhadas serão separadas ou simultâneas
separate=True
separate=False

def oneStep():
      z = random.uniform(0,2*np.pi)  # Metodo simples, didatico para sortear a direcao
    #   if z > 0.75:
    #      dx=0; dy=1 # Norte
    #   elif z > 0.50:
    #      dx=0; dy=-1 # Sul
    #   elif z > 0.25:
    #      dx=1; dy=0 # Leste
    #   else:
    #      dx=-1; dy=0 #  Oeste

      x[iexp]+=np.cos(z)*step
      y[iexp]+=np.sin(z)*step
      #if iexp==0: print(Npassos,iexp,dx,dy,x[iexp],y[iexp])

      if iexp < Nshow: man[iexp].goto(x[iexp],y[iexp])

if separate:
   for iexp in range(Nexp):
      for Npassos in range(NpassosMax):
         oneStep()
else:
   for Npassos in range(NpassosMax):
      for iexp in range(Nexp):
         oneStep()

# Distancia media percorrida nos experimentos
dist  = 0
dist2 = 0
for iexp in range(Nexp):
   d2 = x[iexp]**2+y[iexp]**2
   dist+=sqrt(d2)
   dist2+=d2

media = dist/Nexp
rms = sqrt(dist2/(Nexp-1) - Nexp/(Nexp-1)*media**2 )
      
media/=step
rms/=step

print("Distancia media percorrida em %d experimentos com %d passos: %f  Desvio padrao: %f" %(Nexp,NpassosMax,media,rms) )

wn.exitonclick()

