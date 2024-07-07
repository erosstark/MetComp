"""
Eros Moreira Ferreira
05/06/2024
Le um arquivo com o temperaturas em fahrenheit de cada mes e escreve um arquivo
com as temperaturas convertidas em celsius
"""
import numpy as np

# carregando o arquivo
file_temperaturas_Fahr = open(r"temperaturas_NovaYork_Fahrenheit.txt","r")
lista_file_temperaturas_Fahr = file_temperaturas_Fahr.readlines()
file_temperaturas_Fahr.close()

# tratando os dados do arquivo
meses_ano = []
temperaturas_Fahr = []
for i in lista_file_temperaturas_Fahr:
    if i[0] != '#':
        lines = i.split()
        meses_ano.append(lines[0]); temperaturas_Fahr.append(lines[1])

# função para converter fahrenheit para celsius;
Fahr2Celsius = lambda Tf: (5/9) * (Tf - 32)
temperaturas_celsius = [Fahr2Celsius(float(T)) for T in temperaturas_Fahr]
print(temperaturas_celsius)

# Arquivo output dos dados convertidos.
outfile_celsius = open(r"temperaturas_NovaYork_Celsius.txt", "w")

outfile_celsius.write("mes/ano   temperatura em celsius\n")
for mes, temp in zip(meses_ano, temperaturas_celsius):
    outfile_celsius.write(f"{mes:10} {temp:.1f} °C  \n")
outfile_celsius.close()