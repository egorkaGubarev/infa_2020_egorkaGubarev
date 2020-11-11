from background import Background
from button import Button
from text import Text

# General
background = Background()

# Close
text_close = Text('Close game?', 0, 0)
button_close_cancel = Button('Cancel', 0, 40)
button_close_close = Button('Close', 0, 80)

# Credits
text_credits_egorka = Text('EgorkaGubarev - programmer', 0, 0)
text_credits_polina = Text('PolinaKP - designer, artist, composer', 0, 40)
button_credits_close = Button('Close', 0, 80)

# Menu
text_menu = Text('Space Program', 0, 0)
button_menu_play = Button('Play', 0, 40)
button_menu_tutorials = Button('Tutorials', 0, 80)
button_menu_setting = Button('Settings', 0, 120)
button_menu_credits = Button('Credits', 0, 160)
button_menu_close = Button('Close', 0, 200)

# Tutorials
text_tutorials = Text('No tutorials yet', 0, 0)
button_tutorials_close = Button('Close', 0, 40)
