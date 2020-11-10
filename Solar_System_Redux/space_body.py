"""
Модуль космического тела
"""


class SpaceBody:
    """
    Описывает космическое тело
    """

    def __init__(self, color: tuple, mass: float, name: str, radius: int, speed_x: float, speed_y: float, x: float,
                 y: float):
        """
        Параметры космического тела

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

        # При создании объекта его ускорение обнуляется
        self.acceleration_x: float = 0  # Ускорение вдоль оси x в [м/с^2]
        self.acceleration_y: float = 0  # Ускорение вдоль оси y в [м/с^2]

        self.color: tuple = color
        self.mass: float = mass
        self.name: str = name
        self.radius: int = radius
        self.speed_x: float = speed_x
        self.speed_y: float = speed_y
        self.x: float = x
        self.y: float = y
