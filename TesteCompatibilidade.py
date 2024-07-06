
"""
01/05/2024 
Define o grau de compatibilidade entre duas medidas
"""


from math import sqrt
def compatibilidade(y: float, y1:float, incert_y:float, incert_y1:float):
    """
    Testa a compatibilitade entre duas medidas 
    usando a formula |y-y1|/sqrt(incert_y^2 + incert_y1^2)
    Args:
        y (float): _description_
        y1 (float): _description_
        incert_y (float): _description_
        incert_y1 (float): _description_

    Returns:
        Tuple: Valor do teste, Resultado.
    """
    
    teste = abs((y - y1) / sqrt(incert_y**2 + incert_y1**2))
    if teste <= 1:
        return teste, "Compativeis"
    elif 1 < teste <= 3:
        return teste, "Compativeis com baixa probabilidade"
    elif teste > 3:
        return teste, "Imcompativeis"