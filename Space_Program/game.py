import pygame

from functions import *
from globals import *

pygame.init()


class Game:

    def __init__(self):

        self.clock = pygame.time.Clock()
        self.color_dict: dict = {'black': (0, 0, 0)}
        self.buttons_dict: dict = {'create': [None],
                                   'close': [[button_close_cancel, game_menu],
                                             [button_close_close, game_exit]],
                                   'credits': [[button_credits_close, game_menu]],
                                   'menu': [[button_menu_credits, game_credits],
                                            [button_menu_close, game_close],
                                            [button_menu_play, None],
                                            [button_menu_setting, None],
                                            [button_menu_tutorials, game_tutorials]],
                                   'tutorials': [[button_tutorials_close, game_menu]]}
        self.graphic_objects_dict: dict = {'create': [None],
                                           'close': [background,
                                                     button_close_cancel,
                                                     button_close_close,
                                                     text_close],
                                           'credits': [background,
                                                       button_credits_close,
                                                       text_credits_egorka,
                                                       text_credits_polina],
                                           'menu': [background,
                                                    button_menu_credits,
                                                    button_menu_close,
                                                    button_menu_play,
                                                    button_menu_setting,
                                                    button_menu_tutorials,
                                                    text_menu],
                                           'tutorials': [background,
                                                         text_tutorials,
                                                         button_tutorials_close]}
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
