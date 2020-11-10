"""
Главный модуль
"""

from functions import *
from settings import *

clock = pygame.time.Clock()  # Часы
screen = create_screen(full_screen_mode_status, screen_height, screen_width)  # Создание экрана

# Создание пользовательского интерфейса
user_interface = create_user_interface(clock, colors_dict, fps, screen)

simulation = create_simulation(clock, colors_dict, fps, screen, user_interface)  # Создание симуляции

simulation.setup()
user_interface.setup()

# Пока симуляция не завершена
while simulation.status != 'finish':
    simulation.update_logic()
    simulation.update_physics()
    simulation.update_graphics()
    user_interface.update_buttons()
    simulation.log_information()
