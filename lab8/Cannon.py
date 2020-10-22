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
              (255, 0, 0), # Red
             ]
screen_width = 1519
screen_height = 754
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Logic
clock = pygame.time.Clock()
finished = False

# Interface
ammo_speed_text = 'Start bullet speed [px / s]: '
bullets_amount_text = 'Bullets left: '
bullet_mode = 'shell'
cannon_mode_text = 'Mode: '
font = 'MTCORSVA.TTF'
font_size = 36
shells_amount_text = 'Shells left: '
text_smoothing = True
text_y = 0
tutorial_text_enter = 'Press Enter to start the game'
tutorial_text_escape = 'Press Esc to leave the game'
tutorial_text_l_shift = 'Press left Shift to switch cannon mode'
tutorial_text_mouse = 'Move the mouse to aim the cannon'
tutorial_text_s = 'Press and hold S to decrease bullet speed'
tutorial_text_space = 'Press Space to shoot the cannon'
tutorial_text_w = 'Press and hold W to increase bullet speed'

# --Objects--

# Bullet
bullets_amount = 12
bullet_radius_factor = 4 # Ratio between cannon.height and bullet radius
bullet_speed_factor = 2 # Ratio between bullet speed and cannon.ammo_speed
bullet_params = {'ammo_name': 'bullet', 'amount': bullets_amount, 'radius factor': bullet_radius_factor, 
                 'speed factor': bullet_speed_factor, 'text': bullets_amount_text,}

# Shell
shells_amount = 6
shell_radius_factor = 2 # Ratio between cannon.height and shell radius
shell_speed_factor = 1 # Ratio between shell speed and cannon.ammo_speed
shell_params = {'ammo_name': 'shell', 'amount': shells_amount, 'radius factor': shell_radius_factor,
                'speed factor': shell_speed_factor, 'text': shells_amount_text}

# Ammo
ammo_list = []
ammo_params = {'heavy gun': shell_params, 'machine gun': bullet_params, 'text': shells_amount_text}
ammo_speed = 0
ammo_speed_max = 740
ammo_speed_step = 10

# Cannon
cannon_direction = 0
cannon_height = 25
cannon_mode = 'heavy gun'
cannon_x = 0
cannon_y = screen_height - cannon_height
cannon_width = 100

# Enemy
enemy_amount = 5
enemy_generation_chance = 100 // FPS # 1 enemy per second
enemy_list = []
enemy_min_height = 50
enemy_max_height = 100
enemy_min_speed = 50
enemy_max_speed = 100
enemy_x = screen_width
enemy_min_y = 0
enemy_min_width = 50
enemy_max_width = 100

# Physics
dt = 1/FPS # Integral step in [s]
g = 200 # Free fall acceleration in [px / s^2]

class Ammo:
    '''
    Defines bullet
    '''
    
    def __init__(self, mode: str, radius: int, speed_x: int, speed_y: int, x: int, y: int):
        '''
        Bullet params
        '''
        
        self.color = cannon.color
        self.mode = mode
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.x = x
        self.y = y
        
    def draw(self):
        '''
        Draws bullet on the screen
        '''
        
        circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
    def hit(self):
        '''
        Hits the enemy
        '''
        
        for enemy in enemy_list:
            if (self.x + self.radius > enemy.x and self.x - self.radius < enemy.x + enemy.width and
                self.y + self.radius > enemy.y and self.y - self.radius < enemy.y + enemy.height):
                
                # This is made to prevent double kills
                if self in ammo_list:
                    ammo_list.remove(self)
                enemy_list.remove(enemy)
        
    def move(self):
        '''
        Moves the bullet over the screen
        '''
        
        # Var simplification
        r = self.radius
        
        # If ammo has left the screen
        if self.x < 0 or self.x > screen_width or self.y < 0 or self.y > screen_height:
            ammo_list.remove(self) 
        self.speed_y = self.speed_y + g * dt
        self.x = self.x + self.speed_x * dt
        self.y = self.y + self.speed_y * dt
        self.draw()
        

class Cannon:
    '''
    Defines a cannon
    '''
    
    def __init__(self):
        '''
        Cannon params
        '''
        
        self.ammo_params = ammo_params
        self.ammo_speed = ammo_speed
        self.ammo_speed_max = ammo_speed_max
        self.ammo_speed_step = ammo_speed_step
        self.ammo_speed_text = ammo_speed_text
        self.color = color_list[1] # Green
        self.direction = cannon_direction
        self.font = font
        self.font_size = font_size
        self.height = cannon_height
        self.mode = cannon_mode
        self.mode_text = cannon_mode_text
        self.smoothing = text_smoothing
        self.text_y = text_y
        self.x = cannon_x
        self.y = cannon_y
        self.width = cannon_width
    
    def aim(self):
        '''
        Aims the cannon to the mouse
        '''
        
        aim_x = pygame.mouse.get_pos()[0] # Mouse x
        aim_y = pygame.mouse.get_pos()[1] # Mouse y
        delta_x = aim_x - self.x
        delta_y = self.y - aim_y
        if delta_x != 0: # Prevent crashing if cannon.direction is 90 degrees
            real_direction = m.atan(delta_y / delta_x)
            self.direction = max(0, min(m.pi, real_direction)) # cannon.direction is within 0 to 90 degrees
    
    def charge(self):
        '''
        Increases ammo's speed
        '''
        
        if self.ammo_speed < self.ammo_speed_max:
            self.ammo_speed += self.ammo_speed_step
    
    def discharge(self):
        '''
        Decreases ammo's speed
        '''
        
        if self.ammo_speed > 0: # cannon.ammo_speed can't be negative
            self.ammo_speed -= self.ammo_speed_step
        
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
        
        ammo_speed_text = self.ammo_speed_text + str(self.ammo_speed)
        ammo_amount_text = self.ammo_params[self.mode]['text'] + str(self.ammo_params[self.mode]['amount'])
        mode_text = self.mode_text + str(self.mode)
        font = pygame.font.Font(self.font, self.font_size)
        text_list = [ammo_speed_text, ammo_amount_text, mode_text]
        for text_number in range(len(text_list)):
            text = font.render(text_list[text_number], self.smoothing, self.color)
            
            # Text is printed on the left side of the screen
            screen.blit(text, (0, self.text_y + self.font_size * text_number))
        
    def shoot(self):
        '''
        Shoots the bullet
        '''
        
        # Var simplification
        d = self.direction
        
        # If there is at list 1 ammo of sustainable type
        if self.ammo_params[self.mode]['amount'] > 0:
            ammo_radius = self.height // self.ammo_params[self.mode]['radius factor']
            
            # Cannon nozzle centre
            ammo_x = self.x + int(self.width * m.cos(d) + self.height * (m.sin(d) - m.cos(d)) / 2)
            ammo_y = self.y - int(self.width * m.sin(d) - self.height * (m.cos(d) + m.sin(d)) / 2)
            
            ammo_speed_x = self.ammo_speed * m.cos(d) * self.ammo_params[self.mode]['speed factor']
            ammo_speed_y = -self.ammo_speed * m.sin(d) * self.ammo_params[self.mode]['speed factor']
            ammo_mode = self.ammo_params[self.mode]['ammo_name']
            self.ammo_params[self.mode]['amount'] -= 1 # Spend 1 ammo
            ammo = Ammo(ammo_mode, ammo_radius, ammo_speed_x, ammo_speed_y, ammo_x, ammo_y)
            ammo_list.append(ammo)
            
    def switch_mode(self):
        '''
        Switches shooting system of the cannon
        '''
        
        if self.mode == 'heavy gun':
            self.mode = 'machine gun'
        else:
            self.mode = 'heavy gun'
            

class Enemy:
    '''
    Defines enemies
    '''
    
    def __init__(self, height: int, speed: int, x: int, y: int, width: int):
        '''
        Enemy params
        '''
        
        self.color = color_list[2] # Red
        self.height = height
        self.speed = speed
        self.x = x
        self.y = y
        self.width = width
    
    def draw(self):
        '''
        Draws enemies on the screen
        '''
        
        rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
    def move(self):
        '''
        Moves enemies over the screen
        '''
        
        self.x -= int(self.speed * dt)
        self.draw()

            
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
        self.text_enter = tutorial_text_enter
        self.text_escape = tutorial_text_escape
        self.text_l_shift = tutorial_text_l_shift
        self.text_mouse = tutorial_text_mouse
        self.text_s = tutorial_text_s
        self.text_space = tutorial_text_space
        self.text_w = tutorial_text_w
        self.y = text_y
        
    def show_tutorial(self):
        '''
        Displays control tutorial
        '''
        
        
        skipped = False
        tutorial_text_list = [self.text_w, self.text_s, self.text_mouse, self.text_l_shift,
                              self.text_space, self.text_escape, self.text_enter]
        font = pygame.font.Font(self.font, self.font_size)
        for text_number in range(len(tutorial_text_list)):
            text = font.render(tutorial_text_list[text_number], self.smoothing, self.color)
            
            # Text is printed on the left side of the screen
            screen.blit(text, (0, self.y + self.font_size * text_number))
            
        pygame.display.update()
        while not skipped:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        skipped = True
                        
                        
def generate_enemy(enemy_amount: int):
    '''
    Generates enemies
    '''
    
    for enemy_number in range(enemy_amount):
        height = randint(enemy_min_height, enemy_max_height)
        speed = randint(enemy_min_speed, enemy_max_speed)
        x = enemy_x
        y = randint(enemy_min_y, screen_height - height)
        width = randint(enemy_min_width, enemy_max_width)
        enemy = Enemy(height, speed, x, y, width)
        enemy_list.append(enemy)
            
            
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
    if keys[pygame.K_s]:
        cannon.discharge()
    elif keys[pygame.K_w]:
        cannon.charge()
    if cannon.mode == 'machine gun':
        if keys[pygame.K_SPACE]:
            cannon.shoot()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if cannon.mode == 'heavy gun':
                if event.key == pygame.K_SPACE:
                    cannon.shoot()
            if event.key == pygame.K_LSHIFT:
                cannon.switch_mode()
            if event.key == pygame.K_ESCAPE:
                finished = True
    return finished
            
            
def process_bullets():
    '''
    Manages bullets events
    '''

    for ammo in ammo_list:
        ammo.move()
        ammo.hit()
        
    
def process_cannon():
    '''
    Manages cannon events
    '''
    
    cannon.aim()
    cannon.draw()
    cannon.hud_text()

    
def process_enemy():
    '''
    Manages enemy events
    '''
    
    for enemy in enemy_list:
        enemy.move()
    
    # Generate 1 enemy with defined chance
    chance = randint(1, 100)
    if chance <= enemy_generation_chance:
        generate_enemy(1)
    

process_setup_events()
cannon = Cannon()
while not finished:
    process_bullets()
    process_enemy()
    process_cannon()
    finished = process_screen(finished)
pygame.quit()