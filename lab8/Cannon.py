# Libraries' import
import math as m
import pygame

from pygame.draw import *
from random import *

pygame.init()

# Params

# Graphic
FPS = 24
color_list = [(0, 0, 0), # Black
              (255, 0, 0), # Red
             ]
screen_width = 1519
screen_height = 754
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Logic
clock = pygame.time.Clock()
finished = False

# Interface
font = 'MTCORSVA.TTF'
smoothing = True
text_size = 36

# -Objects-

# Bullet
time_to_live = 10
bullet_list = []

# Cannon
ammo_amount = 50
ammo_text = 'Bullets left: '
ammo_text_x = 0
ammo_text_y = text_size * 2
cannon_direction = 0
cannon_d_text = 'Cannon direction [degrees]: ' # cannon_direction_text
c_d_t_x = 0 # cannon_direction_text_x
c_d_t_y = text_size # cannon_direction_text_y
cannon_max_speed = 740
cannon_speed = 0
cannon_speed_text = 'Start bullet speed [px / s]: '
c_s_t_x = 0 # cannon_speed_text_x
c_s_t_y = 0 # cannon_speed_text_y
cannon_length = 100
cannon_width = 25
cannon_x = 0
cannon_y = screen_height - cannon_width

# Physics
dt = 1/FPS # Integral step in [s]
elasticity_ortogonal = 1 / 2
elasticity_parallel = 3 / 4
g = 200 # Free fall acceleration in [px / s^2]

class Bullet:
    '''
    Defines bullet
    '''
    
    def __init__(self, color: list, speed_x: int, speed_y: int, radius: int, time_to_live: int, x: int, y: int):
        '''
        Bullet params
        color is list of 3 RGB values
        speed is bullet speed after shooting in [px / s]
        radius im [px]
        time_to_live in [s]
        speed_x in [px / s] in x axis
        speed_y in [px / s] in y axis
        Zero point is centre of a bullet
        x is x coordinate of zero point in [px]
        y is y coordinate of zero point in [px]
        '''
        
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.time_to_live = time_to_live * FPS
        self.x = x
        self.y = y
        
    def draw(self):
        '''
        Draws bullet on the screen
        '''
        
        circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
    def decrease_lifetime(self):
        '''
        Decreases time_to_live
        '''
        
        self.time_to_live = self.time_to_live - 1
        
    def move(self):
        '''
        Moves the bullet over the screen
        '''
        
        wall = ''
        if self.x < self.radius or self.x > screen_width - self.radius:
            wall = 'x'
            self.reflect(wall)
        if self.y < self.radius or self.y > screen_height - self.radius:
            wall = 'y'
            self.reflect(wall)
        self.speed_y = self.speed_y + g * dt
        self.x = self.x + self.speed_x * dt
        self.y = self.y + self.speed_y * dt
        self.draw()
        self.decrease_lifetime()
        
    def reflect(self, wall: str):
        '''
        Makes reflections from walls
        speed is 'x' or 'y'
        '''
        
        if wall == 'x':
            self.speed_x = -self.speed_x * elasticity_ortogonal
            self.speed_y = self.speed_y * elasticity_parallel
            if self.x < self.radius:
                self.x = self.radius
            else:
                self.x = screen_width - self.radius
        elif wall == 'y':
            self.speed_y = -self.speed_y * elasticity_ortogonal
            self.speed_x = self.speed_x * elasticity_parallel
            if self.y < self.radius:
                self.y = self.radius
            else:
                self.y = screen_height - self.radius

class Cannon:
    '''
    Defines cannon
    '''
    
    def __init__(self, ammo: int, color_list: list, direction: int, speed: int, length: int, x: int, y: int, width: int):
        '''
        Cannon params
        ammo is amount of bullets left
        color_list is list of all colors in game
        direction is angle belween x axis and nozzle in [degrees]
        speed is bullet speed after shooting in [px / s]
        length in [px]
        Zero point is top point of gun on the side opposite to the nozzle
        x is x coordinate of zero point in [px]
        y is y coordinate of zero point in [px]
        width in [px]
        '''
        
        self.ammo = ammo
        self.color_list = color_list
        self.direction = direction * m.pi / 180
        self.speed = speed
        self.length = length
        self.x = x
        self.y = y
        self.width = width
    
    def aim(self):
        '''
        Aims the cannon to the mouse
        '''
        
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        delta_x = mouse_x - self.x
        delta_y = self.y - mouse_y
        if delta_x != 0:
            real_direction = m.atan(delta_y / delta_x)
            self.direction = max(0, min(m.pi, real_direction))
    
    def charge(self):
        '''
        Increases bullet's speed
        '''
        
        self.speed = self.speed + 10
    
    def discharge(self):
        '''
        Decreases bullet's speed
        '''
        
        self.speed = self.speed - 10
        
    def draw(self):
        '''
        Draws the cannon on the screen
        '''
        
        # Var simplification
        d = self.direction
        l = self.length
        x = self.x
        y = self.y
        w = self.width
        
        colors_amount = len(self.color_list)
        color = self.color_list[randint(1, colors_amount - 1)]
        polygon(screen, color, [(x, y),
                                (x + int(l * m.cos(d)), y - int(l * m.sin(d))),
                                (x + int(l * m.cos(d) + w * m.sin(d)), y - int(l * m.sin(d) - w * m.cos(d))),
                                (x + int(w * m.sin(d)), y + int(w * m.cos(d)))])
        
    def shoot(self):
        '''
        Shoots the bullet
        '''
        
        # Var simplification
        d = self.direction
        
        if self.ammo > 0:
            colors_amount = len(self.color_list)
            color = self.color_list[randint(1, colors_amount - 1)]
            x = self.x + int(self.length * m.cos(d) + self.width * (m.sin(d) - m.cos(d)) / 2)
            y = self.y - int(self.length * m.sin(d) - self.width * (m.cos(d) + m.sin(d)) / 2)
            speed_x = self.speed * m.cos(d)
            speed_y = -self.speed * m.sin(d)
            bullet = Bullet(color, speed_x, speed_y, self.width // 2, time_to_live, x, y)
            bullet_list.append(bullet)
            self.ammo = self.ammo - 1
        
class Text:
    '''
    Defines text information
    '''
    
    def __init__(self, color: list, font: str, size: int, smoothing: bool, text: str, x: int, y: int):
        '''
        Text params
        color_list is 3 RGB values
        font is font of the text
        size in [px]
        smoothing defines if it's needed to smooth the text
        text is message to print
        Zero point is top left point of the text
        x is x coordinate of zero point in [px]
        y is y coordinate of zero point in [px]
        '''
        
        self.color = color
        self.font = font
        self.size = size
        self.smoothing = smoothing
        self.text = text
        self.x = x
        self.y = y
    
    def hud_text(self):
        '''
        Prints text on the screen
        '''
        
        if self.smoothing == True:
            smoothing = 1
        else:
            smoothing = 0
        font = pygame.font.Font(self.font, self.size)
        speed = font.render(self.text, smoothing, self.color)
        screen.blit(speed, (self.x, self.y))
        

cannon = Cannon(ammo_amount, color_list, cannon_direction, cannon_speed, cannon_length, cannon_x, cannon_y, cannon_width)

while not finished:
    clock.tick(FPS)
    screen.fill(color_list[0])
    bullet_speed = Text(color_list[1], font, text_size, smoothing, cannon_speed_text + str(cannon.speed) + ' / ' + str(cannon_max_speed), c_s_t_x, c_s_t_y)
    bullet_d = Text(color_list[1], font, text_size, smoothing, cannon_d_text + str(int(round(cannon.direction * 180 / m.pi))), c_d_t_x, c_d_t_y)
    bullet_amount = Text(color_list[1], font, text_size, smoothing, ammo_text + str(cannon.ammo), ammo_text_x, ammo_text_y)
    bullet_speed.hud_text()
    bullet_d.hud_text()
    bullet_amount.hud_text()
    for bullet in bullet_list:
        if bullet.time_to_live == 0:
            bullet_list.remove(bullet)
    for bullet in bullet_list:
        bullet.move()
    cannon.draw()
    cannon.aim()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and cannon.speed > 0:
                cannon.discharge()
            elif event.key == pygame.K_w and cannon.speed < cannon_max_speed:
                cannon.charge()
            elif event.key == pygame.K_SPACE:
                cannon.shoot()
            elif event.key == pygame.K_ESCAPE:
                finished = True

pygame.quit()