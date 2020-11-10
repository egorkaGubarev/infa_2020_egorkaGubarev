"""
Главный модуль
"""

from functions import *
from settings import *

screen = create_screen(full_screen_mode_status, screen_height, screen_width)  # Создание экрана
simulation = create_simulation(screen)  # Создание симуляции
simulation.setup()

# Пока симуляция не завершена
while simulation.status != 'finish':
    simulation.update_logic()
    simulation.update_physics()
    simulation.update_interface()
    simulation.update_graphics()
    simulation.log_information()
