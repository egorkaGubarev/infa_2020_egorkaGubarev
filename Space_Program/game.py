import pygame

from functions import *
from globals import *

pygame.init()


class Game:

    def __init__(self):

        self.clock = pygame.time.Clock()
        self.color_dict: dict = {'black': (0, 0, 0)}
        self.buttons_dict: dict = {'create': [None],
                                   'close': [[button_cancel, game_close_cancel],
                                             [button_close, game_exit]],
                                   'credits': [[button_credits_close, game_close_cancel]],
                                   'menu': [[button_credits, game_credits],
                                            [button_exit, game_close],
                                            [button_play, None],
                                            [button_setting, None],
                                            [button_tutorials, None]]}
        self.graphic_objects_dict: dict = {'create': [None],
                                           'close': [background,
                                                     button_cancel,
                                                     button_close,
                                                     text_close],
                                           'credits': [background,
                                                       button_credits_close,
                                                       text_credits_egorka,
                                                       text_credits_polina],
                                           'menu': [background,
                                                    button_credits,
                                                    button_exit,
                                                    button_play,
                                                    button_setting,
                                                    button_tutorials,
                                                    text_menu]}
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

        buttons_list: list = self.buttons_dict[self.mode]

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.status: str = 'exit'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button_object in buttons_list:
                    button = button_object[0]
                    button_function = button_object[1]
                    if button.process_click(event):
                        button_function(self)

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
