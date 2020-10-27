# Libraries' import
import math as m
import pygame

from pygame.draw import *
from pygame.mixer import *
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
background = 'background.bmp'

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
music.load('background_music.wav')
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

# Sound
bullet_sound = Sound('bullet.wav')
tank_crack_sound = Sound('tank_crack.wav')
shell_sound = Sound('shell.wav')

# --Objects--

# Bullet
bullets_amount = 12
bullet_height = 6
bullet_image = 'bullet.bmp'
bullet_speed_factor = 2 # Ratio between bullet speed and cannon.ammo_speed
bullet_params = {'ammo_name': bullet_image, 'amount': bullets_amount, 'height': bullet_height,
                 'sound': bullet_sound, 'speed factor': bullet_speed_factor, 'text': bullets_amount_text,}

# Shell
shells_amount = 6
shell_height = 12
shell_image = 'shell.bmp'
shell_speed_factor = 1 # Ratio between shell speed and cannon.ammo_speed
shell_params = {'ammo_name': shell_image, 'amount': shells_amount, 'height': shell_height,
                'sound': shell_sound, 'speed factor': shell_speed_factor, 'text': shells_amount_text}

# Ammo
ammo_list = []
ammo_params = {'heavy gun': shell_params, 'machine gun': bullet_params}
ammo_speed = 0
ammo_speed_max = 740
ammo_speed_step = 10

# Cannon
cannon_direction = 0
cannon_height = 75
cannon_image = 'kv_1_tank.bmp'
cannon_mode = 'heavy gun'
cannon_x = 0
cannon_y = screen_height - cannon_height
cannon_width = 100

# Enemy
enemy_amount = 5
enemy_generation_chance = 100 // FPS # Not more then 2 enemy per second
enemy_list = []
enemy_min_height = 50
enemy_max_height = 100
enemy_min_speed = 50
enemy_max_speed = 100
enemy_x = screen_width
enemy_min_y = screen_height // 2
enemy_min_width = 50
enemy_max_width = 100
enemy_mode_list = ['panther_tank.bmp']

# Physics
dt = 1/FPS # Integral step in [s]
g = 200 # Free fall acceleration in [px / s^2]

class Ammo:
    '''
    Defines bullet
    '''
    
    def __init__(self, mode: str, height: int, speed_x: int, speed_y: int, x: int, y: int):
        '''
        Bullet params
        '''
        
        self.mode = mode
        self.height = height
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.x = x
        self.y = y
        
    def draw(self):
        '''
        Draws bullet on the screen
        '''
        
        surface = pygame.image.load(self.mode)
        scale = surface.get_height() / self.height
        self.width = int(surface.get_width() / scale)
        surface = pygame.transform.scale(surface, (self.width, self.height))
        rect = surface.get_rect(topleft = (self.x, self.y))
        screen.blit(surface, rect)
        
    def hit(self):
        '''
        Hits the enemy
        '''
        
        for enemy in enemy_list:
            if (self.x + self.height > enemy.x and self.x - self.height < enemy.x + enemy.width and
                self.y + self.height > enemy.y and self.y - self.height < enemy.y + enemy.height):
                
                # This is made to prevent double kills
                if self in ammo_list:
                    ammo_list.remove(self)
                enemy_list.remove(enemy)
                tank_crack_sound.play()
        
    def move(self):
        '''
        Moves the bullet over the screen
        '''
        
        # Var simplification
        r = self.height
        
        # If ammo has left the screen
        if self.x < 0 or self.x > screen_width or self.y > screen_height:
            ammo_list.remove(self) 
        self.speed_y = self.speed_y + g * dt
        self.x = self.x + int(self.speed_x * dt)
        self.y = self.y + int(self.speed_y * dt)
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
        self.image = cannon_image
        self.mode = cannon_mode
        self.mode_text = cannon_mode_text
        self.smoothing = text_smoothing
        self.text_y = text_y
        self.x = cannon_x
        self.y = cannon_y
    
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
        
        surface = pygame.image.load(self.image)
        scale = surface.get_height() / self.height
        self.width = int(surface.get_width() / scale)
        surface = pygame.transform.scale(surface, (self.width, self.height))
        rect = surface.get_rect(topleft = (self.x, self.y))
        screen.blit(surface, rect)
        
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
            ammo_height = self.ammo_params[self.mode]['height']
            
            # Cannon nozzle centre
            ammo_x = self.x + 7 * self.width // 8
            ammo_y = self.y + self.height // 4
            
            ammo_speed_x = self.ammo_speed * m.cos(d) * self.ammo_params[self.mode]['speed factor']
            ammo_speed_y = -self.ammo_speed * m.sin(d) * self.ammo_params[self.mode]['speed factor']
            ammo_mode = self.ammo_params[self.mode]['ammo_name']
            self.ammo_params[self.mode]['amount'] -= 1 # Spend 1 ammo
            self.ammo_params[self.mode]['sound'].play()
            ammo = Ammo(ammo_mode, ammo_height, ammo_speed_x, ammo_speed_y, ammo_x, ammo_y)
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
    
    def __init__(self, height: int, speed: int, mode: str, x: int, y: int):
        '''
        Enemy params
        '''
        
        self.height = height
        self.speed = speed
        self.mode = mode
        self.x = x
        self.y = y
        self.width = 0 # Defines in self.draw()
        
    def draw(self):
        '''
        Draws enemies on the screen
        '''
        
        surface = pygame.image.load(self.mode)
        scale = surface.get_height() / self.height
        self.width = int(surface.get_width() / scale)
        surface = pygame.transform.scale(surface, (self.width, self.height))
        rect = surface.get_rect(topleft = (self.x, self.y))
        screen.blit(surface, rect)
        
    def move(self):
        '''
        Moves enemies over the screen
        '''
        
        self.x -= int(self.speed * dt)
        self.draw()
    
    def remove(self):
        '''
        Removes the enemy if he leaves the screen
        '''
        if self.x + self.width < 0:
            enemy_list.remove(self)
            
    def prevent_collision(self):
        '''
        Prevent enemies to be drawn on each other
        '''
        
        for enemy in enemy_list:
            if (self.x + self.width > enemy.x and self.x < enemy.x + enemy.width and
                self.y + self.height > enemy.y and self.y < enemy.y + enemy.height):
                if self.x > enemy.x:
                    self.speed -= 1 / 2
                else:
                    self.speed += 1 / 2
            
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
        modes_amount = len(enemy_mode_list)
        mode = enemy_mode_list[randint(0, modes_amount - 1)] # Random enemy mode
        x = enemy_x
        y = randint(enemy_min_y, screen_height - height)
        overdraw = False
        for enemy in enemy_list:
            if (x > enemy.x and x < enemy.x + enemy.width and
                y + height > enemy.y and y < enemy.y + enemy.height):
                overdraw = True
        if not overdraw:
            enemy = Enemy(height, speed, mode, x, y)
            enemy_list.append(enemy)
            
            
def process_setup_events():
    '''
    Manages setup events
    '''
    
    tutorial = Message()
    tutorial.show_tutorial()
    music.play()
    
            
def process_screen(finished: bool):
    '''
    Manages screen events
    '''
    
    pygame.display.update()
    clock.tick(FPS)
    background_surface = pygame.image.load(background)
    background_surface = pygame.transform.scale(background_surface, (screen_width, screen_height))
    background_rect = background_surface.get_rect(topleft = (0, 0)) # Topleft edge of the screen
    screen.blit(background_surface, background_rect)
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
        enemy.prevent_collision()
    for enemy in enemy_list:
        enemy.remove()
    
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