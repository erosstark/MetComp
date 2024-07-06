# lancamento de um dado

from turtle import width
import numpy as np
import random as rnd
import matplotlib.pyplot as plt

rnd.seed(1)
N = 10**3
x = np.array([rnd.randrange(1,8) for i in range(N+1)])

plt.hist(x, bins = 7, density=True)
plt.grid(True)
plt.show()


