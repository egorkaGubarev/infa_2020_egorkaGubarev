"""
Модуль симуляции
"""

import pygame
import math

from pygame.draw import *

from space_body import SpaceBody


class Simulation:
    """
    Описывает симуляцию
    """

    def __init__(self, clock, colors_dict: dict, fps: int, screen, user_interface):
        """
        Параметры симуляции

        clock - часы
        colors_dict - словарь цветов
        fps - частота обновления экрана в [Гц]
        screen - экран для рисования
        user_interface - объект пользовательского интерфейса
        """

        self.clock = clock
        self.colors_dict: dict = colors_dict
        self.fps: int = fps
        self.time_scale = 5000000  # Отношение скорости течения времени в симуляции к физической
        self.dt: float = 1 / fps * self.time_scale  # Шаг времени в симуляции в [с]
        self.init_file_name: str = 'init.txt'  # Файл для чтения информации
        self.log_file_name: str = 'log.txt'  # Файл для записи информации
        self.scale = None  # Определяется в методе self.count_scale
        self.screen = screen
        self.space_bodies_list: list = []  # Список космических тел
        self.status: str = 'Created'  # Симуляция создана
        self.user_interface = user_interface

    def convert_coordinates(self, space_body):
        """
        Преобразует физические координаты в [м] в экранные в [px]

        Центральная экранная система координат:
        Начало - центр экрана
        Ось x горизонтально вправо
        Ось y вертикально вверх

        Экранная система координат:
        Начало - верхний левый угол экрана
        Ось x горизонтально вправо
        Ось y вертикально вниз

        space_body - космическое тело, координаты которого надо преобразовать
        """

        scale: float = self.scale  # Масштаб в [м/px]
        screen_height: int = pygame.display.get_surface().get_size()[1]  # Высота экрана в [px]
        screen_width: int = pygame.display.get_surface().get_size()[0]  # Ширина экрана в [px]
        x: float = space_body.x  # Физическая координата тела по оси x в [м]
        y: float = space_body.y  # Физическя координата тела по оси y в [м]

        screen_x_center: int = int(x / scale)  # Центральная экранная координата тела по оси x в [px]
        screen_y_center: int = int(y / scale)  # Центральная экранная координата тела по оси y в [px]
        screen_x: int = screen_x_center + screen_width // 2  # Экранная координата тела по оси x в [px]
        screen_y: int = screen_height // 2 - screen_y_center  # Экранная координата тела по оси y в [px]

        # Словарь экранных координат в [px]
        screen_coordinates: dict = {'x': screen_x, 'y': screen_y}

        return screen_coordinates

    @staticmethod
    def count_distance(x_1: float, x_2: float, y_1: float, y_2: float):
        """
        Вычисляет расстояние между 2 точками

        x_1 - x коодината 1 точки
        x_2 - x координата 2 точки
        y_1 - y координата 1 точки
        y_2 - у координата 2 точки
        """

        distance: float = math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)  # Расстояние между точками
        return distance

    def count_scale(self):
        """
        Вычисляет масштаб графического окна в [м/px]
        """

        screen_height: int = pygame.display.get_surface().get_size()[1]  # Высота экрана в [px]
        screen_width: int = pygame.display.get_surface().get_size()[0]  # Ширина экрана в [px]
        space_bodies_list: list = self.space_bodies_list  # Список космических тел

        # Свободное экранное пространство по горизонтали в [px]
        sun_available_distance_x: float = screen_width // 2

        sun_available_distance_y: float = screen_height // 2  # Свободное экранное пространство по вертикали в [px]

        # Свободное экранное пространство в [px]
        sun_available_distance: float = min(sun_available_distance_x, sun_available_distance_y)

        max_sun_distance: float = 0  # Максимальное возможное физическое расстояние от Солнца до тела [м]
        for space_body in space_bodies_list:
            x: float = space_body.x  # Физическая координата тела по оси x в [м]
            y: float = space_body.y  # Физическая координата тела по оси y в [м]
            sun_distance: float = self.count_distance(0, x, 0, y)  # Физическое расстояние от Солнца до тела в [м]
            if sun_distance > max_sun_distance:
                max_sun_distance: float = sun_distance  # Поиск максимального физического расстояния до Солнца в [м]
        scale: float = max_sun_distance / sun_available_distance  # Масштаб в [м/px]
        return scale

    def create_log_file(self):
        """
        Создаёт файл для записи информации
        """

        log_file_name: str = self.log_file_name  # Имя файла для записи информации

        log = open(log_file_name, 'w')  # Файл для записи информации
        log.close()

    def create_space_body(self, color: tuple, mass: float, name: str, radius: int, speed_x: float, speed_y: float,
                          x: float, y: float):
        """
        Создаёт космическое тело

        Физическая система координат:
        Начало координат - центр экрана
        Ось x горизонтально вправо
        Ось y вертикально вверх

        color - цвет в формате RGB
        mass - масса в [кг]
        name - название
        radius - экранный радиус в [px]
        speed_x - физическая скорость вдоль оси x в [м/с]
        speed_y - физическая скорость вдоль оси y в [м/с]
        x - физическая координата x в [м]
        y - физическая координата y в [м]
        """

        new_space_body = SpaceBody(color, mass, name, radius, speed_x, speed_y, x, y)
        self.space_bodies_list.append(new_space_body)

    def log_information(self):
        """
        Записывает информацию о симуляции в файл
        """

        status: str = self.status  # Статус
        if status == 'run':  # Если симуляция запущена
            log_file_name: str = self.log_file_name  # Имя файла для записи информации
            space_bodies_list: list = self.space_bodies_list  # Список космических тел

            log = open(log_file_name, 'a')  # Файл для записи информации
            for space_body in space_bodies_list:
                print('Name -> ' + str(space_body.name)+'; X -> ' + str(space_body.x) + '; Y -> ' + str(space_body.y) +
                      '; Speed_x -> ' + str(space_body.speed_x) + '; Speed_y -> ' + str(space_body.speed_y), file=log)
            print('--- Simulation cycle ---', file=log)
            log.close()

    def read_information(self):
        """
        Читает информацию о симуляции из файла и преобразует её в подхлдящий формат
        """

        init_file_name: str = self.init_file_name  # Имя файла для чтения информации

        init = open(init_file_name, 'r')  # Файл для чтения информации
        for new_space_body in init:
            new_space_body_params: str = new_space_body  # Строка с параметрами нового космического тела
            new_space_body_params_stripped = new_space_body_params.strip()  # Строка без символа конца строки

            # Список строк с параметрами нового космического тела
            new_space_body_params_separated = new_space_body_params_stripped.split(';')

            color_string: str = new_space_body_params_separated[0]  # Строка с цветом тела в формате RGB
            color_string_components: list = color_string.split(',')  # Строка с компонентами цвета в формате RGB
            color_red_sting: str = color_string_components[0]  # Строка с красной компонентой цвета
            color_green_sting: str = color_string_components[1]  # Строка с зелёной компонентой цвета
            color_blue_sting: str = color_string_components[2]  # Строка с синей компонентой цвета
            color_red: int = int(color_red_sting)  # Красная компонента цвета
            color_green: int = int(color_green_sting)  # Зелёная компонента цвета
            color_blue: int = int(color_blue_sting)  # Синяя компонента цвета
            color: tuple = (color_red, color_green, color_blue)  # Цвет тела в формате RGB
            mass_string: str = new_space_body_params_separated[1]  # Строка с массой тела в [кг]
            mass: float = float(mass_string)  # Масса тела в [кг]
            name_string: str = new_space_body_params_separated[2]  # Строка с названием тела
            name: str = name_string[1:]  # Название тела без пробела в начале
            radius_string: str = new_space_body_params_separated[3]  # Строка с экранным радиусом тела в [px]
            radius: int = int(radius_string)  # Экранный радиус тела в [px]
            if name != 'Sun':

                # Строка с физической скоростью тела вдоль оси x в [м/с]
                speed_x_string: str = new_space_body_params_separated[4]

                speed_x: float = float(speed_x_string)  # Физическая скорость тела вдоль оси x в [м/с]

                # Строка с физической скоростью тела вдоль оси y в [м/с]
                speed_y_string: str = new_space_body_params_separated[5]

                speed_y: float = float(speed_y_string)  # Физическая скорость тела вдоль оси y в [м/с]

                # Строка с физической координатой тела по оси x в [м]
                x_string: str = new_space_body_params_separated[6]

                x: float = float(x_string)  # Физическая координата тела по оси x в [м]

                # Строка с физической координатой тела по оси y в [м]
                y_string: str = new_space_body_params_separated[7]

                y: float = float(y_string)  # Физическая координата тела по оси y в [м]
            else:

                #  По определению физических координат и скоростей, у Солнца они нулевые
                speed_x: float = 0
                speed_y: float = 0
                x: float = 0
                y: float = 0

            self.create_space_body(color, mass, name, radius, speed_x, speed_y, x, y)
        init.close()

    def setup(self):
        """
        Начальные действия при запуске симуляции
        """

        self.status: str = 'run'  # Симуляция запущена
        self.read_information()
        self.scale = self.count_scale()  # Масштаб в [м/px]
        self.create_log_file()

    def update_logic(self):
        """
        Обрабатывает логические события в симуляции
        """

        user_interface = self.user_interface
        clock = self.clock  # Часы
        fps: int = self.fps  # Частота обновления экрана в [Гц]

        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # Если нажата кнопка
                if event.key == pygame.K_ESCAPE:  # Если нажат Esc
                    self.status: str = 'finish'  # Симуляция завершена
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Если нажата кнопка мыши
                user_interface.process_buttons(event, self)

    def update_graphics(self):
        """
        Обрабатывает графические события в симуляции
        """

        colors_dict: dict = self.colors_dict  # Словарь цветов
        screen = self.screen  # Экран для рисования
        space_bodies_list: list = self.space_bodies_list  # Список космических тел

        pygame.display.update()
        screen.fill(colors_dict['black'])
        for space_body in space_bodies_list:

            # Словарь экранных координат в [px]
            screen_coordinates: dict = self.convert_coordinates(space_body)

            screen_x: int = screen_coordinates['x']  # Экранная координата вдоль оси x в [px]
            screen_y: int = screen_coordinates['y']  # Экранная координата вдоль оси y в [px]
            circle(screen, space_body.color, (screen_x, screen_y), space_body.radius)

            if space_body.name != 'Sun':
                space_body.draw(screen_x, screen_y, screen, colors_dict['black'])

    def update_physics(self):
        """
        Обрабатывает физические события в симуляции
        """

        grav_const = 6.6743015 * 10 ** (-11)  # Гравитационная постоянная
        status: str = self.status  # Статус симуляции

        if status == 'run':  # Если симуляция запущена
            for space_body_1 in self.space_bodies_list:
                acceleration_x = space_body_1.acceleration_x
                acceleration_y = space_body_1.acceleration_y
                for space_body_2 in self.space_bodies_list:
                    if space_body_1 != space_body_2:
                        x_1 = space_body_1.x
                        x_2 = space_body_2.x
                        y_1 = space_body_1.y
                        y_2 = space_body_2.y
                        distance = self.count_distance(x_1, x_2, y_1, y_2)
                        force = grav_const * space_body_1.mass * space_body_2.mass / distance ** 2
                        acceleration = force / space_body_1.mass

                        if x_2 > x_1:
                            angle = math.atan((y_2 - y_1) / (x_2 - x_1))
                        elif x_2 < x_1:
                            angle = math.atan((y_2 - y_1) / (x_2 - x_1)) - math.pi
                        else:
                            if y_1 > y_2:
                                angle = math.pi * 3 / 2
                            elif y_1 < y_2:
                                angle = math.pi / 2
                            else:
                                angle = None

                        if space_body_2.name != "Sun" and space_body_1.name == "Sun":
                            space_body_2.angle = angle
                            space_body_2.distance = distance

                        if type(angle) == float:
                            acceleration_x += acceleration * math.cos(angle)
                            acceleration_y += acceleration * math.sin(angle)
                space_body_1.speed_x += acceleration_x * self.dt
                space_body_1.speed_y += acceleration_y * self.dt
                space_body_1.x += space_body_1.speed_x * self.dt
                space_body_1.y += space_body_1.speed_y * self.dt
