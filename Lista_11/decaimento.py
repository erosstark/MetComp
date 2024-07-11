#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
tau  = 3.053*60
func_pdf = lambda t: (np.log(2)/tau) * 2 ** (-t/tau)
func_cdf = lambda t: 1 - 2 ** (-t/tau)
invert_cdf = lambda x: -tau * np.log(1-x) / np.log(2)

uniform_sample = np.random.uniform(0,0.989999,1000)
samples = [invert_cdf(i) for i in uniform_sample]

plt.hist(samples, bins = 20, density = True)

t = np.linspace(0, 1000, 1000)
plt.plot(t, func_pdf(t),"r")
plt.ylabel("numero de atomos")
plt.xlabel('tempo (s)')
plt.show()

""" 
Ajustar o limite do uniform sample

"""




# %%
