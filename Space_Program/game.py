import pygame

from dictionaries import *
from globals import *

pygame.init()


class Game:

    def __init__(self):

        self.clock = pygame.time.Clock()
        self.color_dict: dict = {'black': (0, 0, 0)}
        self.fps: int = 30  # in [Hz]
        self.language = 'english'
        self.mode: str = 'create'
        self.music_volume: int = 50  # in [%]
        self.sound_volume: int = 50  # in [%]
        self.screen_height: int = 700  # in [px]
        self.screen_width: int = 1200  # in [px]
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        self.graphic_objects_dict: dict = graphic_objects_dict

    def setup(self):

        self.mode: str = 'menu'

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
        graphic_objects_list: list = self.graphic_objects_dict[self.mode]
        screen = self.screen

        clock.tick(fps)
        screen.fill(black)
        for graphic_object in graphic_objects_list:
            if graphic_object is not None:
                graphic_object.draw(screen)
        pygame.display.update()
