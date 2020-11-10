"""
Модуль космического тела
"""

import math

from pygame.draw import *


class SpaceBody:
    """
    Описывает космическое тело
    """

    def __init__(self, color: tuple, mass: float, name: str, radius: int, speed_x: float, speed_y: float, x: float,
                 y: float):
        """
        Параметры космического тела

        angle - угол между осью х и прямой, соединяющей центр планеты и Солнца в [рад]
        acceleration_x - ускорение вдоль оси x в [м/с^2]
        acceleration_y - ускорение вдоль оси y в [м/с^2]
        color - цвет в формате RGB
        mass - масса в [кг]
        name - название
        radius - экранный радиус в [px]
        Начало координат - центр экрана
        Ось x горизонтально вправо
        Ось y вертикально вверх
        speed_x - физическая скорость по оси x в [м/с]
        speed_y - физическая скорость по оси y в [м/с]
        x - физическая координата центра по оси x в [м]
        y - физическая координата центра по оси y в [м]
        """

        self.angle: float = 0
        # При создании объекта его ускорение обнуляется
        self.acceleration_x: float = 0
        self.acceleration_y: float = 0
        self.color: tuple = color
        self.mass: float = mass
        self.name: str = name
        self.radius: int = radius
        self.speed_x: float = speed_x
        self.speed_y: float = speed_y
        self.x: float = x
        self.y: float = y

    def draw(self, x: float, y: float, screen, color: tuple):
        """
        Высчитывает координаты точек, которые не должны быть овещены Солнцем и перекрашивает их в цвет экрана.
        """
        angle = self.angle
        r = self.radius

        x_1 = x - r * math.sin(angle)
        y_1 = y - r * math.cos(angle)
        x_2 = x + r * math.sin(angle)
        y_2 = y + r * math.cos(angle)
        x_3 = x_2 + r * math.cos(angle)
        y_3 = y_2 - r * math.sin(angle)
        x_4 = x_1 + r * math.cos(angle)
        y_4 = y_1 - r * math.sin(angle)

        polygon(screen, color, ((x_1, y_1),
                                (x_2, y_2),
                                (x_3, y_3),
                                (x_4, y_4)))
