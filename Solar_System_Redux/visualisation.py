"""
Модуль визуализации. Нигде, кроме этого модуля, не используются экранные координаты объектов. Функции,
создающие графические объекты и перемещающие их на экране, принимают физические координаты
"""

from pygame.draw import *
from pygame.font import *

font_color: tuple = (0, 255, 0)  # Цвет шрифта - зелёный
font_size: int = 36  # Размер шрифта в [px]
header_font: str = 'Arial-16'  # Шрифт в заголовке
smoothing: bool = True  # Необходимость сглаживания текста
window_height: int = 900  # Высота окна в [px]
window_width: int = 1500  # Ширина окна в [px]
header_x: int = window_width // 2  # Экранная координата x заголовка в [px]
header_y: int = 0  # Экранная координата y заголовка в [px]


def calculate_scale_factor(max_distance: int):
    """
    Вычисляет отношение экранных координат к физическим в [px/м]
    max_distance - максимальное расстояние между планетами в [м]
    """

    max_window_size: int = max(window_height, window_width)  # Максимальный размер графического окна в [px]
    scale_factor: float = max_window_size / max_distance  # Отношение экранных координат к физическим в [px/м]
    return scale_factor


def scale_x(scale_factor: float, x: int):
    """
    Возвращает экранную x координату по физической x координате модели
    scale_factor - отношение экранных координат к физическим в [px/м]
    Начало координат - верхний левый угол экрана
    Ось x горизонтально вправо
    Ось y вертикально вниз
    x - физическая координата модели в [м]
    """

    x: int = int(x * scale_factor)  # Экранная координата x в [px]
    return x


def scale_y(scale_factor: float, y: int):
    """Возвращает экранную y координату по физической y координате модели.
    scale_factor - отношение экранных координат к физическим в [px/м]
    Начало координат - верхний левый угол экрана
    Ось x горизонтально вправо
    Ось y вертикально вниз
    y - физическая координата модели в [м]
    """

    y: int = int(y * scale_factor)  # Экранная координата y в [px]
    return y


def create_body_image(body, scale_factor: float, screen):
    """
    Создаёт отображаемый объект космического тела
    body — объект космического тела
    scale_factor - отношение экранных координат к физическим в [px/м]
    screen — экран для рисования
    """

    color: tuple = body.color  # Цвет тела в формате RGB
    radius: int = body.radius  # Экранный радиус тела в [px]
    x: int = body.x  # Физическая координата x центра тела в [м]
    y: int = body.y  # Физическая координата y центра тела в [м]
    x: int = scale_x(scale_factor, x)  # Экранная координата x центра тела в [px]
    y: int = scale_y(scale_factor, y)  # Экранная координата y центра тела в [px]
    circle(screen, color, (x, y), radius)


def update_system_name(screen, system_name: str):
    """
    Создаёт на экране текст с названием системы небесных тел. Если текст уже был, обновляет его содержание
    screen — экран для рисования.
    system_name — название системы тел
    """

    font = Font(header_font, font_size)
    text = font.render(system_name, smoothing, font_color)
    screen.blit(text, (header_x, header_y))


def update_object_position(body, scale_factor: float, screen):
    """
    Перемещает отображаемый объект на экране
    body — тело, которое нужно переместить
    screen — экран для рисования
    """

    color: tuple = body.color
    radius: int = body.radius  # Экранный радиус тела в [px]
    x: int = body.x  # Физическая координата x центра тела в [м]
    y: int = body.y  # Физическая координата y центра тела в [м]
    x: int = scale_x(scale_factor, x)  # Экранная координата x центра тела в [px]
    y: int = scale_y(scale_factor, y)  # Экранная координата y центра тела в [px]
    circle(screen, color, (x, y), radius)
