
import sys
from traceback import print_tb

# Input das notas.
P1, P2, PF = float(input("Notas da P1: ")) , float(input("Notas da P2: ")),\
    float(input("Notas da PF: "))

if 0 <= (P1 and P2 and PF) <= 10:  # verifica se as notas inseridas são validas.
    media = (P1 + P2 + (2 * PF)) / 4
    # Verifica se foi aprovado ou não.
    if media >= 5:
        print(f"O aluno foi aprovado com média: {media:.1f}")
    else: 
        print(f"O aluno foi reprovado com média: {media:.1f}")
else:
    sys.exit("As notas devem estar entre 0 e 10")