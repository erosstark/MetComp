#%%
#import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Definindo a função gaussiana
def gaussiana(x, a, b, c):
    return a * np.exp(-(x - b)**2 / (2 * c**2))

# Gerando dados de exemplo
x_data = np.linspace(-5, 5, 100)
y_data = gaussiana(x_data, 3, 0, 1) + 0.2 * np.random.normal(size=x_data.size)

# Ajustando a gaussiana aos dados
popt, pcov = curve_fit(gaussiana, x_data, y_data, p0=[3, 0, 1])

# Extraindo os parâmetros ajustados
a_fit, b_fit, c_fit = popt

# Plotando os dados e o ajuste
plt.scatter(x_data, y_data, label='Dados')
x_fit = np.linspace(-5, 5, 1000)
y_fit = gaussiana(x_fit, *popt)
plt.plot(x_fit, y_fit, color='red', label='Ajuste Gaussiano')
plt.legend()
plt.show()
#%%