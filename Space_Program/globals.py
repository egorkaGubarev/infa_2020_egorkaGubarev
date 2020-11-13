from background import Background
from button import Button
from slider import Slider
from text import Text

# General
background = Background()

# Close
text_close = Text('Close game?', 0, 0)
button_close_cancel = Button('mode', ['menu'], ['Cancel'], 0, 40)
button_close_close = Button('mode', ['exit'], ['Close'], 0, 80)

# Credits
text_credits_egorka = Text('EgorkaGubarev - programmer', 0, 0)
text_credits_polina = Text('PolinaKP - designer, artist, composer', 0, 40)
button_credits_close = Button('mode', ['menu'], ['Close'], 0, 80)

# Menu
text_menu = Text('Space Program', 0, 0)
button_menu_play = Button('mode', [None], ["Play !Haven't work yet!"], 0, 40)
button_menu_tutorials = Button('mode', ['tutorials'], ['Tutorials'], 0, 80)
button_menu_setting = Button('mode', ['settings'], ['Settings'], 0, 120)
button_menu_credits = Button('mode', ['credits'], ['Credits'], 0, 160)
button_menu_close = Button('mode', ['close'], ['Close'], 0, 200)

# Settings
text_settings_sound = Text('Sound', 0, 0)
slider_settings_sound = Slider('sound_volume', 50, 10, 50)
text_settings_music = Text('Music', 0, 100)
slider_settings_music = Slider('music_volume', 50, 10, 150)
text_setting_fps = Text('Fps', 0, 200)
button_settings_fps = Button('fps', [60, 30], ['30', '60'], 0, 240)
text_setting_language = Text('Language', 0, 280)
button_settings_language = Button('language', ['english', 'russian'], ["!Haven't work yet!"], 0, 320)
button_settings_close = Button('mode', ['menu'], ['Close'], 0, 360)

# Tutorials
text_tutorials = Text('No tutorials yet', 0, 0)
button_tutorials_close = Button('mode', ['menu'], ['Close'], 0, 40)
