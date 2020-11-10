"""
Модуль пользовательского интерфейса
"""

from button import Button


class UserInterface:
    """
    Описывает пользовательский интерфейс
    """

    def __init__(self, clock, colors_dict: dict, fps: int, screen):
        """
        Параметры интерфейса

        clock - часы
        colors_dict - словарь цветов
        fps - Частота обновления экрана в [Гц]
        screen - экран для рисования
        simulation - объект симуляции
        """

        self.clock = clock
        self.button_list: list = []  # Список кнопок
        self.colors_dict: dict = colors_dict
        self.fps: int = fps
        self.screen = screen
        self.simulation = None  # FIXME добавить комментарий

    def create_buttons(self):
        """
        Создаёт кнопки
        Координата кнопки - координата её верхнего левого угла
        """

        color = self.colors_dict['dark_blue']  # Тёмно-синий цвет кнопки
        height: int = 30  # Высота кнопки 30 [px]
        pause_x: int = 0  # Экранная координата x кнопки паузы в [px]
        pause_y: int = 0  # Экранная координата y кнопки паузы в [px]
        width: int = 30  # Ширина кнопки 30 [px]

        pause_button = Button(self.set_pause, color, height, width, pause_x, pause_y)  # Кнопка паузы

        self.button_list.append(pause_button)

    def process_buttons(self, event, simulation):
        """
        Обрабатывает нажатия кнопок

        event - событие pygame
        simulation - объект симуляции
        """

        button_list: list = self.button_list  # Список кнопок
        self.simulation = simulation  # Присвоение атрибута

        for button in button_list:
            if button.check_click(event.pos):
                button.click_handler()

    def set_pause(self):
        """
        Ставит симуляцию на паузу
        """

        simulation = self.simulation  # Обект симуляции

        if simulation.status == 'run':
            simulation.status = 'pause'
        elif simulation.status == 'pause':
            simulation.status = 'run'

    def update_buttons(self):
        """
        Обновляет изображения кнопок
        """

        button_list: list = self.button_list  # Список кнопок
        screen = self.screen  # Экран для рисования

        for button in button_list:
            button.draw(screen)

    def setup(self):
        """
        Действия при создании интерфейса

        simulation - обект
        """

        self.create_buttons()
