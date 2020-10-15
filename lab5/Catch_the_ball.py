# Libraries import
import math as m
import pygame
from pygame.draw import *
from pygame.mixer import *
from random import *
import time
pygame.init()

# Params

# Auxilary
clock = pygame.time.Clock()
finished = False
object_list = []
start_time = time.time()

# Screen
FPS = 24
screen_width = 1500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# ---Objects---

# Satellites     
start_satellites_amount = 5
create_sound = ''
satellite_delete_sound = Sound('satellite_delete_sound.wav')
min_direction = 0
max_direction = 2 * m.pi
min_height = 25
max_height = 50
score_per_click = 1
min_speed = 5
max_speed = 10
type_satellite = 'glonass.bmp'
test_surface = pygame.image.load(type_satellite)
height = test_surface.get_height()
width = test_surface.get_width()
y_x_ratio = height / width
satellite_params_list = [create_sound, satellite_delete_sound, min_direction, max_direction, min_height, max_height,
                         score_per_click, min_speed, max_speed, type_satellite, y_x_ratio]


# Rockets
rocket_generation_chance = 20 # Probability of generation after clicking on satellite
rocket_create_sound = Sound('rocket_launch_sound.wav')
rocket_delete_sound = Sound('rocket_delete_sound.wav')
min_direction = m.pi / 2
max_direction = m.pi / 2
min_height = 100
max_height = 200
score_per_click = 10
min_speed = 15
max_speed = 40
type_rocket = 'soyuz-rocket-2.bmp'
test_surface = pygame.image.load(type_satellite)
height = test_surface.get_height()
width = test_surface.get_width()
y_x_ratio = height / width
rocket_params_list = [rocket_create_sound, rocket_delete_sound, min_direction, max_direction, min_height, max_height,
                      score_per_click, min_speed, max_speed, type_rocket, y_x_ratio]

# General object data
object_params_list = [satellite_params_list, rocket_params_list]
object_type_list = [satellite_params_list[9], rocket_params_list[9]]

# ---Sound---

music.load('background_music.wav')
rocket_create_sound.set_volume(0.01)
rocket_delete_sound.set_volume(0.01)
satellite_delete_sound.set_volume(0.01)
music.set_volume(0.01)

# ---User interface---
game_time = 30
leader_amount = 5
score = 0

def generate_object(object_list: list, object_type: str):
    '''
    Generates object on the screen
    object_list is list of all objects in game
    object_type is name of *.bmp file with object's image
    '''
    
    index = object_type_list.index(object_type)
    object_params = object_params_list[index]
    create_sound = object_params[0]
    delete_sound = object_params[1]
    direction = object_params[2] + random() * (object_params[3] - object_params[2])
    height = randint(object_params[4], object_params[5])
    score = object_params[6]
    speed = randint(object_params[7], object_params[8])
    width = int(height / object_params[10])
    x = randint(0, screen_width - width)
    if object_type == 'glonass.bmp':
        y = randint(0, screen_height - height)
    elif object_type == 'soyuz-rocket-2.bmp':
        y = screen_height
    if create_sound != '':
        create_sound.play()
    object_list.append([delete_sound, direction, height, object_type, score, speed, width, x, y])


def make_reflection(obj: list):
    '''
    Returns an angle in rads between x axis and object's speed direction after the reflection
    obj is list of object params
    '''
    
    direction = obj[1]
    height = obj[2]
    width = obj[6]
    x = obj[7]
    y = obj[8]
    if x < 0:
        direction = random() * m.pi - m.pi / 2
    elif x > screen_width - width:
        direction = random() * m.pi + m.pi / 2
    elif y < 0:
        direction = random() * m.pi - m.pi
    elif y > screen_height - height:
        direction = random() * m.pi
    return direction
    
    
def count_score(obj: list):
    '''
    Checks if click has occured inside the object
    obj is list with object params
    object_list is list of all objects in game
    '''
    
    click_x = event.pos[0]
    click_y = event.pos[1]
    delete_sound = obj[0]
    height = obj[2]
    object_type = obj[3]
    delta_score = obj[4]
    width = obj[6]
    x = obj[7]
    y = obj[8]
    if click_x >= x and click_x <= x + width and click_y >= y and click_y <= y + height:
        object_list.remove(obj)
        delete_sound.play()
        if object_type == type_satellite:
            generate_object(object_list, type_satellite)
        if object_type != type_rocket and rocket_needed():
            generate_object(object_list, type_rocket)
    else:
        delta_score = 0
    new_score = score + delta_score
    return new_score


def check_time():
    '''
    Checks if the game time is over
    '''
    
    
    if time.time() - start_time > game_time:
        return True
    else:
        return False
    
    
def draw_object(height: int, object_type: str, x: int, y: int):
    '''
    Draws an object on the screen
    height is vertical size of the object in pixels
    object_type is name of *.bmp file with object's image
    zero-point is top-ledt point of rectangle, witch contains an object
    x is x coordinate of zero-point in pixels
    y is y coordinate of zero-point in pixels
    '''
    
    object_surface = pygame.image.load(object_type)
    scale = object_surface.get_height() / height
    width = int(object_surface.get_width() / scale)
    object_surface = pygame.transform.scale(object_surface, (width, height))
    object_rect = object_surface.get_rect(topleft = (x, y))
    screen.blit(object_surface, object_rect)
    
    
def move_object(obj: list):
    '''
    Moves an object over the screen
    obj is list with object params
    '''
    
    direction = obj[1]
    height = obj[2]
    object_type = obj[3]
    speed = obj[5]
    x = obj[7]
    y = obj[8]
    if object_type == type_satellite:
        direction = make_reflection(obj)
    x = int(x + speed * m.cos(direction))
    y = int(y - speed * m.sin(direction))
    draw_object(height, object_type, x, y)
    obj[1] = direction
    obj[7] = x
    obj[8] = y

    
def rocket_needed():
    '''
    Returns 'True' if rocket is needed to generate
    '''
    
    rocket_generation = randint(1, 100) # Random chance generation
    if rocket_generation <= rocket_generation_chance:
        return True
    else:
        return False

def set_leaderboard(score: int):
    '''
    Sves player result to the leaderboard
    score is score amount of player
    '''
    
    leader_list = []
    output = open('leaderboard.txt', 'r')
    for line in output:
        line = line.strip()
        leader_list.append(line)
    output.close()
    leader_list = sort_leaderboard(leader_list)
    output = open('leaderboard.txt', 'w')
    for leader in leader_list:
        print(leader, file = output)
    output.close()
    

def sort_leaderboard(leader_list: list):
    '''
    Sorts leaderboard
    leader_list is list to sort
    '''
    leader_data = []
    leader_score = []
    current_time = time.asctime()
    leader_list.append('Time -> '+str(current_time)+'; score -> '+str(score))
    for leader in leader_list:
        leader_score.append(int(leader[43:])) # Part of string with score as int number
        leader_data.append(leader[:43]) # Another part of string
    for i in range(len(leader_score) - 1): # Sort
        for j in range(i+1, len(leader_score)):
            if leader_score[j] > leader_score[i]:
                swap = leader_score[i]
                leader_score[i] = leader_score[j]
                leader_score[j] = swap
                swap = leader_data[i]
                leader_data[i] = leader_data[j]
                leader_data[j] = swap
    leader_list = []
    for i in range(len(leader_data)):
        leader_list.append(leader_data[i]+str(leader_score[i]))
    leader_list = leader_list[0:leader_amount]
    return leader_list


object_list = []
music.play()
for satellite in range(start_satellites_amount):
    generate_object(object_list, type_satellite)
while not finished:
    clock.tick(FPS)
    for obj in object_list:
        move_object(obj)
    pygame.display.update()
    screen.fill([0, 0, 0])
    finished = check_time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for obj in object_list:
                score = count_score(obj)
pygame.quit()
set_leaderboard(score)
print(score)