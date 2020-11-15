"""
Модуль яблока
"""


class Apple(object):
    """
    Описывает яблоко
    """

    def __init__(self, x: float, y: float):
        """
        Параметры

        Физика
        Координаты центра яблока
        x - координата x яблока в [м]
        y - координата y яблока в [м]

        Графика
        screen - экран pygame
        """

        self.color: tuple = (5, 95, 23)  # Цвет яблока
        self.radius: int = 5  # Радиус яблока в [px]
        self.x: float = x
        self.y: float = y
