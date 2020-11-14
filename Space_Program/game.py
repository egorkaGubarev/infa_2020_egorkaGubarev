import pygame

from pygame.font import *

from dictionaries import *
from globals import *

pygame.init()


class Game:

    def __init__(self):

        self.clock = pygame.time.Clock()
        self.color_dict: dict = {'black': (0, 0, 0)}
        self.font_name: str = 'times.ttf'
        self.font_size: int = 36
        self.fps: int = 30  # in [Hz]
        self.graphic_objects_dict: dict = graphic_objects_dict
        self.language: str = 'English'
        self.language_latest = None
        self.language_english_dict: dict = language_english_dict
        self.language_russian_dict: dict = language_russian_dict
        self.mode: str = 'create'
        self.music_volume: int = 50  # in [%]
        self.screen_height: int = 700  # in [px]
        self.screen_width: int = 1200  # in [px]
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        self.settings_file_name: str = 'settings.txt'
        self.show_information_dict: dict = show_information_dict
        self.smoothing: bool = True
        self.sound_volume: int = 50  # in [%]
        self.text_color: tuple = (128, 0, 0)

    def load_settings(self):

        settings_file_name: str = self.settings_file_name
        settings_file = open(settings_file_name, 'r')
        self.fps: int = int(settings_file.readline())
        language_raw: str = settings_file.readline()
        language: str = language_raw.strip()
        if language == 'English':
            self.language: str = language
            print('English')
        elif language == 'Russian':
            self.language = 'Русский'
            print('Русский')
        self.music_volume: int = int(settings_file.readline())
        self.sound_volume: int = int(settings_file.readline())

    def save_settings(self):

        language: str = self.language
        settings_file_name: str = self.settings_file_name
        settings_file = open(settings_file_name, 'w')
        print(self.fps, file=settings_file)
        if language == 'English':
            print(self.language, file=settings_file)
        elif language == 'Русский':
            print('Russian', file=settings_file)
        print(self.music_volume, file=settings_file)
        print(self.sound_volume, file=settings_file)
        settings_file.close()

    def setup(self):

        self.language_latest = 'English'
        self.mode: str = 'menu'
        self.load_settings()
        self.update_settings()

    def show_information(self):
        font_name: str = self.font_name
        font_size: int = self.font_size
        font = Font(font_name, font_size)
        mode: str = self.mode
        information_list = self.show_information_dict[mode]
        screen = self.screen
        smoothing: bool = self.smoothing
        text_color: tuple = self.text_color

        for info in information_list:
            if info[0] is not None:
                text_str_raw: str = str(info[0])
                text_str_cooked: str = str(vars(self)[text_str_raw])
                text = font.render(text_str_cooked, smoothing, text_color)
                x: int = info[1]  # in [px]
                y: int = info[2]  # in [px]
                screen.blit(text, (x, y))

    def translate(self):
        language: str = self.language
        language_latest: str = self.language_latest

        if language != language_latest:
            if language == 'English':
                for mode in self.graphic_objects_dict:
                    graphic_objects_list: list = self.graphic_objects_dict[mode]
                    for graphic_object in graphic_objects_list:
                        if isinstance(graphic_object, Button) or isinstance(graphic_object, Text):
                            text_str_raw: str = graphic_object.text_str
                            if text_str_raw is not None:
                                text_str_translated: str = language_english_dict[text_str_raw]
                                graphic_object.text_str = text_str_translated
            elif language == 'Русский':
                for mode in self.graphic_objects_dict:
                    graphic_objects_list: list = self.graphic_objects_dict[mode]
                    for graphic_object in graphic_objects_list:
                        if isinstance(graphic_object, Button) or isinstance(graphic_object, Text):
                            text_str_raw: str = graphic_object.text_str
                            if text_str_raw is not None:
                                text_str_translated: str = language_russian_dict[text_str_raw]
                                graphic_object.text_str = text_str_translated
        self.language_latest = language

    def update_logic(self):

        graphic_objects_list: list = self.graphic_objects_dict[self.mode]

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.mode: str = 'exit'
            for graphic_object in graphic_objects_list:
                if isinstance(graphic_object, Button) or isinstance(graphic_object, Slider):
                    if graphic_object.value is not None:
                        if graphic_object.process_click(event):
                            vars(self)[graphic_object.parameter] = graphic_object.value

    def update_graphics(self):

        black: tuple = self.color_dict['black']
        clock = self.clock
        fps: int = self.fps  # in [Hz]
        mode: str = self.mode
        graphic_objects_list: list = self.graphic_objects_dict[mode]
        screen = self.screen

        clock.tick(fps)
        screen.fill(black)
        for graphic_object in graphic_objects_list:
            if graphic_object is not None:
                graphic_object.draw(screen)
        self.show_information()
        pygame.display.update()

    def update_settings(self):
        fps: int = self.fps
        music_volume: int = self.music_volume
        sound_volume: int = self.sound_volume
        if fps == 30:
            button_settings_fps.value_index = 0
        elif fps == 60:
            button_settings_fps.value_index = 1
        slider_settings_music.value = music_volume
        slider_settings_sound.value = sound_volume
