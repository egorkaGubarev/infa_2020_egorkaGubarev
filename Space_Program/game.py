import pygame

from globals import *

pygame.init()


class Game:

    def __init__(self):

        self.clock = pygame.time.Clock()
        self.color_dict: dict = {'black': (0, 0, 0)}
        self.graphic_objects_dict: dict = {'create': [None],
                                           'menu': [background,
                                                    button_authors,
                                                    button_exit,
                                                    button_play,
                                                    button_setting,
                                                    button_tutorial]}
        self.fps: int = 24  # in [Hz]
        self.mode: str = 'create'
        self.screen_height: int = 700  # in [px]
        self.screen_width: int = 1200  # in [px]
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        self.status: str = 'create'

    def setup(self):

        self.mode: str = 'menu'
        self.status: str = 'run'

    def update_logic(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.status: str = 'exit'

    def update_graphics(self):

        black: tuple = self.color_dict['black']
        clock = self.clock
        fps: int = self.fps  # in [Hz]
        graphic_objects_dict: dict = self.graphic_objects_dict
        mode: str = self.mode
        screen = self.screen

        clock.tick(fps)
        screen.fill(black)
        for graphic_object in graphic_objects_dict[mode]:
            graphic_object.draw(screen)
        pygame.display.update()
