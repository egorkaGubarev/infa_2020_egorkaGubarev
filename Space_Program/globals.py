from background import Background
from button import Button
from slider import Slider
from text import Text

# General
background = Background()

# Close
text_close = Text('Close game?', 0, 0)
button_close_cancel = Button('mode', 'Cancel', ['menu'], 0, 40)
button_close_close = Button('mode', 'Close', ['exit'], 0, 80)

# Create world
button_create_world_main_menu = Button('mode', 'Main menu', ['menu'], 0, 200)

# Credits
text_credits_egorka = Text('EgorkaGubarev - programmer', 0, 0)
text_credits_polina = Text('PolinaKP - designer, artist, composer', 0, 40)
button_credits_close = Button('mode', 'Close', ['menu'], 0, 80)

# Language
button_language_close_english = Button('mode', None, ['settings'], 0, 0)
button_language_english = Button('language', 'English', ['English'], 0, 0)
button_language_close_russian = Button('mode', None, ['settings'], 0, 40)
button_language_russian = Button('language', 'Russian', ['Russian'], 0, 40)

# Menu
text_menu = Text('Space Program', 0, 0)
button_menu_play = Button('mode', 'Play', ['create world'], 0, 40)
button_menu_tutorials = Button('mode', 'Tutorials', ['tutorials'], 0, 80)
button_menu_setting = Button('mode', 'Settings', ['settings'], 0, 120)
button_menu_credits = Button('mode', 'Credits', ['credits'], 0, 160)
button_menu_close = Button('mode', 'Close', ['close'], 0, 200)

# Settings
text_settings_sound = Text('Sound', 0, 0)
slider_settings_sound = Slider('sound_volume', 50, 10, 50)
text_settings_music = Text('Music', 0, 100)
slider_settings_music = Slider('music_volume', 50, 10, 150)
text_setting_fps = Text('Fps', 0, 200)
button_settings_fps = Button('fps', None, [60, 30], 0, 240)
text_settings_language = Text('Language', 0, 280)
button_settings_language = Button('mode', None, ['language'], 0, 320)
button_settings_close = Button('mode', 'Close', ['menu'], 0, 360)

# Tutorials
text_tutorials = Text('No tutorials yet', 0, 0)
button_tutorials_close = Button('mode', 'Close', ['menu'], 0, 40)
