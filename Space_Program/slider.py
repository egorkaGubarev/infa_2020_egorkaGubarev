import pygame

from pygame.draw import *

from text import Text


class Slider:

    def __init__(self, parameter, value: int, x: int, y: int):
        """
        Zero point is top left
        x in [px]
        y in [px]
        """

        # Scale
        self.parameter = parameter
        self.color_active: tuple = (0, 0, 128)
        self.color_passive: tuple = (0, 0, 0)
        self.height: int = 30  # in [px]
        self.width_full: int = 200  # in [px]
        self.x: int = x  # in [px]
        self.y: int = y  # in [px]

        # Handle
        self.handle_height: int = 40  # in [px]
        self.handle_transparent_border: int = 30  # in [px]
        self.handle_width: int = 10  # in [px]

        # Value
        self.value: int = value  # in [%]
        self.value_space: int = 10  # in [px]

    def draw(self, screen):

        # Scale
        color_active: tuple = self.color_active
        color_passive: tuple = self.color_passive
        height: int = self.height  # in [px]
        width_full: int = self.width_full  # in [px]
        width_active: int = int(width_full * self.value / 100)  # in [px]
        width_passive: int = round(width_full * (1 - self.value / 100))  # in [px]
        x: int = self.x  # in [px]
        x_passive: int = x + width_active  # in [px]
        y: int = self.y  # in [px]

        rect(screen, color_active, (x, y, width_active, height))
        rect(screen, color_passive, (x_passive, y, width_passive, height))

        # Handle
        handle_height: int = self.handle_height  # in [px]
        handle_width: int = self.handle_width  # in [px]
        handle_x: int = x + width_active - handle_width // 2  # in [px]
        handle_y: int = y - (handle_height - height) // 2  # in [px]

        rect(screen, color_active, (handle_x, handle_y, handle_width, handle_height))

        # Value
        value_space: int = self.value_space  # in [px]
        value_str: str = str(self.value)
        value_x: int = x + width_full + value_space  # in [px]
        value_text = Text(value_str, value_x, y)

        value_text.draw(screen)

    def process_click(self, event):

        # Slider
        height: int = self.height  # in [px]
        width_full: int = self.width_full  # in [px]
        width_active: int = int(self.value / 100 * width_full)  # in [px]
        x: int = self.x  # in [px]
        y: int = self.y  # in [px]

        # Handle
        handle_height: int = self.handle_height  # in [px]
        handle_width: int = self.handle_width  # in [px]
        h_t_b: int = self.handle_transparent_border
        handle_x: int = x + width_active - handle_width // 2  # in [px]
        handle_y: int = y - (handle_height - height) // 2  # in [px]

        # Mouse
        m_x: int = event.pos[0]  # in [px]
        m_y: int = event.pos[1]  # in [px]
        mouse_value: int = m_x - x  # in [px]
        mouse_value_scaled: int = 100 * mouse_value // width_full  # in [%]

        if handle_x - h_t_b <= m_x <= handle_x + handle_width + h_t_b and handle_y <= m_y <= handle_y + handle_height:
            if pygame.mouse.get_pressed()[0]:
                self.value: int = max(0, min(mouse_value_scaled, 100))  # in [%]
            return True
        else:
            return False
