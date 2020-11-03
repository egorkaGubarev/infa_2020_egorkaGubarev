"""
Модуль типов данных. Содержит типы данных, описывающих звезду и планету
"""


class Star:
    """
    Тип данных, описывающий звезду. Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    def __init__(self, color: list, image: str, mass: int, radius: int, speed_x: int, speed_y: int, x: int, y: int):
        """
        Параметры звезды
        color - цвет звезды в формате RGB
        image - название файла с изображением звезды
        mass - масса звезды в [кг]
        radius - радиус звезды в [м]
        Начало координат - верхний левый угол экрана
        Ось x горизонтально вправо
        Ось y вертикально вниз
        speed_x - скорость по оси x в [м/с]
        speed_y - скорость по оси y в [м/с]
        x - координата по оси x в [м]
        y - координата по оси y в [м]
        """

        self.color = color
        self.image = image
        self.mass = mass
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.type = 'star'  # Признак объекта звезды
        self.x = x
        self.y = y


class Planet:
    """
    Тип данных, описывающий планету. Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    def __init__(self, color: list, image: str, mass: int, radius: int, speed_x: int, speed_y: int, x: int, y: int):
        """
        Параметры планеты
        color - цвет планеты в формате RGB
        image - название файла с изображением планеты
        mass - масса планеты в [кг]
        radius - радиус планеты в [м]
        Начало координат - верхний левый угол экрана
        Ось x горизонтально вправо
        Ось y вертикально вниз
        speed_x - скорость по оси x в [м/с]
        speed_y - скорость по оси y в [м/с]
        x - координата по оси x в [м]
        y - координата по оси y в [м]
        """

        self.color = color
        self.image = image
        self.mass = mass
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.type = 'planet'  # Признак объекта планеты
        self.x = x
        self.y = y
