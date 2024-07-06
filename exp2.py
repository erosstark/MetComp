""" 
01/05/2024
Analisa dados obtidos do gráfico a mao do exp2 de fisexp2
"""


from parametrosReta import inclinacao, intersecta
from numpy.lib.scimath import sqrt

# Pontos do gráfico.
y = 8.9*10**-2
y0 = 6.3*10**-2
x = 84.4
x0 = 61.2

print("\n----------------------------\n")

# coef linear e angular
a = inclinacao(x0,y0,x,y)
incert_a = 5*a/100
b = intersecta(x0,y0,x,y)
incert_b = 5*b/100
print(f"{a = }\n{incert_a = }\n{b = }\n{incert_b = }")

print("\n----------------------------\n")

# Gravidade(cm/s^2)
g_referencia: float = 9.7875
incert_g_referencia: float = 0.0001
g = 1/a
print(f"{g = :.10f}")
incert_g = incert_a / a ** 2
print(f"{incert_g = }")

print("\n----------------------------\n")


# Raio da bola (cm)
raio = b*g
print(f"{raio = :}")
incert_raio = sqrt((g*incert_b)**2 + (b*incert_g)**2)
print(f"incerteza do raio {incert_raio}")

print("\n----------------------------\n")

# Precisao
precisao_g_referencia = incert_g_referencia/g_referencia
precisao_g = incert_g/g
precisao_raio = abs(incert_raio/raio)
print(f"{precisao_g_referencia = : %}\n{precisao_g = : %}\n{precisao_raio =: %}")


print("\n----------------------------\n")

"""
============================================================= 
g a partir daqui passa a estar em m/s^2 e o raio em m.
"""
g = g/100 ; incert_g = incert_g/100             # convertendo para m/s^2

raio = raio/100 ; incert_raio = incert_raio/100
raio_referencia: float = 1.510/100 ; incert_raio_referencia: float = 0.003/100

g_referencia: float = 9.7875 ; incert_g_referencia: float = 0.0001

# Acurácia
acuracia_g = abs((g-g_referencia)/g_referencia)
print(f"{acuracia_g =: %}") 



print("\n-----------------------------\n")


# Compatibilidade com o valor referência
from TesteCompatibilidade import compatibilidade

compatibilidade_g_grafico = compatibilidade(g, g_referencia, incert_g, incert_g_referencia)

print(f"Compatibilidade entre g do gráfico e g referência\n\
{compatibilidade_g_grafico}\n")

g_qtiplot: float = 9.0
incert_g_qtiplot: float = 0.2
compatibilidade_g_qtiplot = compatibilidade(g_qtiplot, g_referencia, incert_g_qtiplot, incert_g_referencia)

print(f"Compatibilidade entre g qtiplot e g referencia\n\
{compatibilidade_g_qtiplot}\n")

# Compatibilidade entre os resultados.
raio_qtiplot = -0.045
incert_raio_qtiplot = 0.009
compatibilidade_g = compatibilidade(g, g_qtiplot, incert_g, incert_g_qtiplot)

print(f"Compatibilidade entre g do gráfico e do qtiplot\n{compatibilidade_g}\n")
compatibilidade_raio = compatibilidade(raio, raio_qtiplot, incert_raio, incert_raio_qtiplot)
print(f"Compatibilidade entre raio do gráfico e do qtiplot\
\n{compatibilidade_raio}\n")

""" 
============================================================
"""
