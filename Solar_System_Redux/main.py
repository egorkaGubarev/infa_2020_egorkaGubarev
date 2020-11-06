"""
Главный модуль
"""

from settings import *

simulation.setup()
while simulation.status == 'run':
    simulation.update_logic()
    simulation.update_physics()
    simulation.update_graphics()
    simulation.log_information()
