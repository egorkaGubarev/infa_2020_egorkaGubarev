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
              (0, 255, 0), # Green
             ]
screen_width = 1519
screen_height = 754
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Logic
clock = pygame.time.Clock()
finished = False

# Interface
bullets_amount_text = 'Bullets left: '
bullet_speed_text = 'Start bullet speed [px / s]: '
font = 'MTCORSVA.TTF'
font_size = 36
text_smoothing = True
text_x = 0
text_y = 0
tutorial_text_w = 'Press and hold W to increase bullet speed'
tutorial_text_s = 'Press and hold S to decrease bullet speed'
tutorial_text_mouse = 'Move the mouse to aim the cannon'
tutorial_text_space = 'Press SPACE to shoot the cannon'
tutorial_text_escape = 'Press ESCAPE to leave the game'
tutorial_text_enter = 'Press ENTER to start the game'

# -Objects-

# Bullet
bullets_amount = 50
bullet_list = []
bullet_speed = 0
bullet_speed_max = 740
bullet_speed_step = 1
bullet_time_to_live = 10

# Cannon
cannon_direction = 0
cannon_height = 25
cannon_x = 0
cannon_y = screen_height - cannon_height
cannon_width = 100

# Physics
dt = 1/FPS # Integral step in [s]
elasticity_ortogonal = 1 / 2
elasticity_parallel = 3 / 4
g = 200 # Free fall acceleration in [px / s^2]

class Bullet:
    '''
    Defines bullet
    '''
    
    def __init__(self, speed_x: int, speed_y: int, x: int, y: int):
        '''
        Bullet params
        '''
        
        self.color = cannon.color
        self.radius = cannon.height // 2
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.time_to_live = bullet_time_to_live * FPS
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
        
        # Var simplification
        r = self.radius
        
        if self.x < r or self.x > screen_width - r or self.y < r or self.y > screen_height - r:
            self.reflect()
        self.speed_y = self.speed_y + g * dt
        self.x = self.x + self.speed_x * dt
        self.y = self.y + self.speed_y * dt
        self.decrease_lifetime()
        self.draw()
        
    def reflect(self):
        '''
        Makes reflections from walls
        '''
        
        if self.x < self.radius or self.x > screen_width - self.radius:
            self.speed_x = -self.speed_x * elasticity_ortogonal
            self.speed_y = self.speed_y * elasticity_parallel
            if self.x < self.radius:
                self.x = self.radius
            else:
                self.x = screen_width - self.radius
        if self.y < self.radius or self.y > screen_height - self.radius:
            self.speed_x = self.speed_x * elasticity_parallel
            self.speed_y = -self.speed_y * elasticity_ortogonal
            if self.y < self.radius:
                self.y = self.radius
            else:
                self.y = screen_height - self.radius

class Cannon:
    '''
    Defines a cannon
    '''
    
    def __init__(self):
        '''
        Cannon params
        '''
        
        self.bullets_amount = bullets_amount
        self.bullets_amount_text = bullets_amount_text
        self.bullet_speed = bullet_speed
        self.bullet_speed_max = bullet_speed_max
        self.bullet_speed_step = bullet_speed_step
        self.bullet_speed_text = bullet_speed_text
        self.bullet_time_to_live = bullet_time_to_live
        self.color = color_list[1] # Green
        self.direction = cannon_direction
        self.font = font
        self.font_size = font_size
        self.height = cannon_height
        self.smoothing = text_smoothing
        self.text_x = text_x
        self.text_y = text_y
        self.x = cannon_x
        self.y = cannon_y
        self.width = cannon_width
    
    def aim(self):
        '''
        Aims the cannon to the mouse
        '''
        
        aim_x = pygame.mouse.get_pos()[0]
        aim_y = pygame.mouse.get_pos()[1]
        delta_x = aim_x - self.x
        delta_y = self.y - aim_y
        if delta_x != 0:
            real_direction = m.atan(delta_y / delta_x)
            self.direction = max(0, min(m.pi, real_direction))
    
    def charge(self):
        '''
        Increases bullet's speed
        '''
        
        if self.bullet_speed < self.bullet_speed_max:
            self.bullet_speed = self.bullet_speed + self.bullet_speed_step
    
    def discharge(self):
        '''
        Decreases bullet's speed
        '''
        
        if self.bullet_speed > 0:
            self.bullet_speed = self.bullet_speed - self.bullet_speed_step
        
    def draw(self):
        '''
        Draws the cannon on the screen
        '''
        
        # Var simplification
        d = self.direction
        h = self.height
        x = self.x
        y = self.y
        w = self.width
        
        polygon(screen, self.color, [(x, y),
                                     (x + int(w * m.cos(d)), y - int(w * m.sin(d))),
                                     (x + int(w * m.cos(d) + h * m.sin(d)), y - int(w * m.sin(d) - h * m.cos(d))),
                                     (x + int(h * m.sin(d)), y + int(h * m.cos(d)))])
        
    def hud_text(self):
        '''
        Texsts the main cannon's params on the screen
        '''
        
        bullet_speed_text = self.bullet_speed_text + str(self.bullet_speed)
        bullets_amount_text = self.bullets_amount_text + str(self.bullets_amount)
        font = pygame.font.Font(self.font, self.font_size)
        text_list = [bullet_speed_text, bullets_amount_text]
        for text_number in range(len(text_list)):
            text = font.render(text_list[text_number], self.smoothing, self.color)
            screen.blit(text, (self.text_x, self.text_y + self.font_size * text_number))
        
    def shoot(self):
        '''
        Shoots the bullet
        '''
        
        # Var simplification
        d = self.direction
        
        if self.bullets_amount > 0:
            bullet_radius = self.height // 2
            bullet_x = self.x + int(self.width * m.cos(d) + self.height * (m.sin(d) - m.cos(d)) / 2)
            bullet_y = self.y - int(self.width * m.sin(d) - self.height * (m.cos(d) + m.sin(d)) / 2)
            bullet_speed_x = self.bullet_speed * m.cos(d)
            bullet_speed_y = -self.bullet_speed * m.sin(d)
            bullet = Bullet(bullet_speed_x, bullet_speed_y, bullet_x, bullet_y)
            bullet_list.append(bullet)
            self.bullets_amount = self.bullets_amount - 1

            
class Message:
    '''
    Defines text messages on the screen
    '''
    
    def __init__(self):
        '''
        Messages params
        '''
        
        self.color = color_list[1] # Green
        self.font = font
        self.font_size = font_size
        self.smoothing = text_smoothing
        self.text_w = tutorial_text_w
        self.text_s = tutorial_text_s
        self.text_mouse = tutorial_text_mouse
        self.text_space = tutorial_text_space
        self.text_escape = tutorial_text_escape
        self.text_enter = tutorial_text_enter
        self.x = text_x
        self.y = text_y
        
    def show_tutorial(self):
        '''
        Displays control tutorial
        '''
        
        
        skipped = False
        tutorial_text_list = [self.text_w, self.text_s, self.text_mouse,
                              self.text_space, self.text_escape, self.text_enter]
        font = pygame.font.Font(self.font, self.font_size)
        for text_number in range(len(tutorial_text_list)):
            text = font.render(tutorial_text_list[text_number], self.smoothing, self.color)
            screen.blit(text, (self.x, self.y + self.font_size * text_number))
        pygame.display.update()
        while not skipped:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        skipped = True
            
            
def process_setup_events():
    '''
    Manages setup events
    '''
    
    tutorial = Message()
    tutorial.show_tutorial()
    
            
def process_screen(finished: bool):
    '''
    Manages screen events
    '''
    
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(color_list[0])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s] and cannon.bullet_speed > 0:
        cannon.discharge()
    elif keys[pygame.K_w]:
        cannon.charge()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cannon.shoot()
            if event.key == pygame.K_ESCAPE:
                finished = True
    return finished
            
            
def process_bullets():
    '''
    Manages bullets events
    '''

    for bullet in bullet_list:
        if bullet.time_to_live == 0:
            bullet_list.remove(bullet)
    for bullet in bullet_list:
        bullet.move()
        
    
def process_cannon():
    '''
    Manages cannon events
    '''
    
    cannon.aim()
    cannon.draw()
    cannon.hud_text()
        

process_setup_events()
cannon = Cannon()
while not finished:
    finished = process_screen(finished)
    process_cannon()
    process_bullets()
pygame.quit()