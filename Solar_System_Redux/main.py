"""
Главный модуль
"""

from settings import *

simulation.setup()
while simulation.status != 'finish':
    simulation.update_logic()
    simulation.update_physics()
    simulation.update_interface()
    simulation.update_graphics()
    simulation.log_information()
