#%%
from turtle import pendown
from turtles3D import Turtle3D
import numpy as np
import time
#%%
t = Turtle3D()
s = t.getscreen
    
#%%    
#%%
fxy = lambda x,y : np.cos(x)

x = np.linspace(1, 100, 500)
y = np.linspace(1, 100, 500)
z = fxy(x,y)

axessize = 100
#desenha  = graph(t,x,y,z)
t.pendown()
t.pencolor("blue")
t.goto(axessize, 0, 0)
t.write("X")
t.goto(-axessize, 0, 0)
t.write("-X")
t.home()
t.pencolor("red")
t.goto(0, axessize, 0)
t.write("Y")
t.goto(0, -axessize, 0)
t.write("-Y")
t.home()
t.pencolor("green")
t.goto(0, 0, axessize)
t.write("Z")
t.goto(0, 0, -axessize)
t.write("-Z")
t.home()
t.pencolor("black")
# %%

for i in range(len(x)):
    t.goto(float(x[i]),float(y[i]),float(z[i]))
t.penup()
t.home()
t.rotateX(50,False)
t.rotateY(50,False)
for g in range(1000):
    t.rotateZ(1)
    time.sleep(1/60)
