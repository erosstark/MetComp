""" 
Eros Moreira Ferreira
24/04/2024

Calcula o coeficiente angular e linear de uma reta
dado a coordenada de dois pontos.
"""

def inclinacao(x1 , y1, x2, y2)->float:
    """
    Calcula o coeficiente angular de uma reta dado dois pontos.

    Args:
        x1, y1, x2, y2 (float): coordenadas dos pontos 1 e 2.

    Returns:
        float: Coeficiente angular.
    """
    return (y2-y1) / (x2-x1)


def intersecta(x1, y1, x2, y2)->float:
    """
    Calcula o coeficiente linear de uma reta dado um ponto.

    Args:
        x, y (float): Pontos da reta

    Returns:
        float: Coeficiente linear
    """
    return  y1-((y2-y1) / (x2-x1)) * x1

# Recebe as coordenadas dos pontos e transforma em float.
x1, y1 = input("Coordenadas do ponto 1 separadas por virgula: ").split(",")
x2, y2 = input("Coordenadas do ponto 2 separadas por virgula: ").split(",")
x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

# Coeficiente linear e angular a partir das funções
a = inclinacao(x1, y1, x2, y2)
b = intersecta(x1, y1, x2, y2)

# Exibe osr resultados.
print(f"ponto {x1,y1} e {x2,y2}")
print(f"coeficiente angular {a = :.1f}")
print(f"coeficiente linear {b = :.1f}")
print(f"Equação da reta y = {a:.1f}x + {b:.1f}")

""" 
Resultados dos testes para alguns valores:
    
    ponto (-1.0, -5.0) e (0.0, 0.0)
    coeficiente angular a = 5.0
    coeficiente linear b = 0.0
    Equação da reta y = 5.0x + 0.0
    
    ponto (5.0, 5.0) e (1.0, 1.0)
    coeficiente angular a = 1.0
    coeficiente linear b = 0.0
    Equação da reta y = 1.0x + 0.0

    ponto (-1.0, -5.0) e (-3.0, -2.0)
    coeficiente angular a = -1.5
    coeficiente linear b = -6.5
    Equação da reta y = -1.5x + -6.5

    ponto (1.0, 5.0) e (2.0, 7.0)
    coeficiente angular a = 2.0
    coeficiente linear b = 3.0
    Equação da reta y = 2.0x + 3.0
    
    ponto (1.0, 3.1) e (-4.3, 2.5)
    coeficiente angular a = 0.1
    coeficiente linear b = 3.0
    Equação da reta y = 0.1x + 3.0
"""



