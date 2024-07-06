""" 
Eros Moreira Ferreira
24/04/2024

Calcula o coeficiente angular e linear de uma reta
dado a coordenada de dois pontos.
"""

def inclinacao(x1, y1, x2, y2)->float:
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




