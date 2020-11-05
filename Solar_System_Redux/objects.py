"""
Модуль типов данных. Содержит классы
"""

import pygame


class Simulation:
    """
    Описывает симуляцию
    """

    def __init__(self):
        """
        Параметры симуляции
        """

        self.clock = pygame.time.Clock()  # Часы
        self.fps: int = 24  # 24 кадра в секунду
        self.init_file_name: str = 'init.txt'  # Файл для чтения информации
        self.log_file_name: str = 'log.txt'  # Файл для записи информации
        self.screen_height: int = 800  # Высота экрана 800 [px]
        self.screen_width: int = 1500  # Ширина экрана 1500 [px]
        self.space_bodies_list: list = []  # Список космических тел
        self.status: str = 'Created'  # Симуляция создана

    def convert_coordinates(self):
        """
        Преобразует физические координаты и скорости в [м] и [м/с] в экранные в [px] и [px/с]
        """

        # FIXME Надо сделать egorkaGubarev

        pass

    def create_log_file(self):
        """
        Создаёт файл для записи информации
        """

        log = open(self.log_file_name, 'w')  # Файл для записи информации
        log.close()

    def create_screen(self):
        """
        Создаёт экран
        """

        screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        return screen

    def create_space_body(self, color: tuple, mass: float, name: str, radius: int, speed_x: float, speed_y: float,
                          x: float, y: float):
        """
        Создаёт космическое тело

        color - цвет в формате RGB
        mass - масса в [кг]
        name - название
        radius - экранный радиус в [px]
        Начало координат - верхний левый угол экрана
        Ось x горизонтально вправо
        Ось y вертикально вниз
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

        log = open(self.log_file_name, 'a')
        for space_body in self.space_bodies_list:
            print('Name -> ' + str(space_body.name)+'; X -> ' + str(space_body.x) + '; Y -> ' + str(space_body.y) + ';',
                  file=log)
        print('--- Simulation cycle ---', file=log)
        log.close()

    def read_information(self):
        """
        Читает информацию о симуляции из файла и преобразует её в подхлдящий формат
        """

        init = open(self.init_file_name, 'r')  # Файл для чтения информации
        for new_space_body in init:
            new_space_body_params: str = new_space_body  # Строка с параметрами нового космического тела
            new_space_body_params_stripped = new_space_body_params.strip()  # Строка без символа конца строки

            # Список строк с параметрами нового космического тела
            new_space_body_params_separated = new_space_body_params_stripped.split(';')

            color_string: str = new_space_body_params_separated[0]  # Строка с цветом тела в формате RGB
            color: tuple = tuple(color_string)  # Цвет тела в формате RGB
            mass_string: str = new_space_body_params_separated[1]  # Строка с массой тела в [кг]
            mass: float = float(mass_string)  # Масса тела в [кг]
            name: str = new_space_body_params_separated[2]  # Название тела
            radius_string: str = new_space_body_params_separated[3]  # Строка с экранным радиусом тела в [px]
            radius: int = int(radius_string)  # Экранный радиус тела в [px]

            # Строка с физической скоростью тела вдоль оси x в [м/с]
            speed_x_string: str = new_space_body_params_separated[4]

            speed_x: float = float(speed_x_string)  # Физическая скорость тела вдоль оси x в [м/с]

            # Строка с физической скоростью тела вдоль оси y в [м/с]
            speed_y_string: str = new_space_body_params_separated[5]

            speed_y: float = float(speed_y_string)  # Физическая скорость тела вдоль оси y в [м/с]

            # Строка с физической координатой тела по оси x в [м]
            x_string: str = new_space_body_params_separated[5]

            x: int = int(x_string)  # Физическая координата тела по оси x в [м]

            # Строка с физической координатой тела по оси y в [м]
            y_string: str = new_space_body_params_separated[5]

            y: int = int(y_string)  # Физическая координата тела по оси y в [м]
            self.create_space_body(color, mass, name, radius, speed_x, speed_y, x, y)
        init.close()

    def setup(self):
        """
        Начальные действия при запуске симуляции
        """

        self.status: str = 'run'  # Симуляция запущена
        self.read_information()
        self.create_log_file()

    def update_logic(self):
        """
        Обрабатывает логические события в симуляции
        """

        self.clock.tick(self.fps)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.status: str = 'finish'  # Симуляция завершена

    def update_graphics(self):
        """
        Обрабатывает графические события в симуляции
        """

        # FIXME Надо сделать egorkaGubarev

        pass

    def update_physics(self):
        """
        Обрабатывает физические события в симуляции
        """

        # FIXME Надо сделать PolinaKP

        pass


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
        Начало координат - верхний левый угол экрана
        Ось x горизонтально вправо
        Ось y вертикально вниз
        speed_x - физическая скорость по оси x в [м/с]
        speed_y - физическая скорость по оси y в [м/с]
        x - физическая координата центра по оси x в [м]
        y - физическая координата центра по оси y в [м]
        """

        self.color: tuple = color
        self.mass: float = mass
        self.name: str = name
        self.radius: int = radius
        self.speed_x: float = speed_x
        self.speed_y: float = speed_y
        self.x: float = x
        self.y: float = y
