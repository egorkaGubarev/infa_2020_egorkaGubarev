from background import Background
from button import Button
from text import Text

# General
background = Background()

# Close
text_close = Text('Close game?', 0, 0)
button_cancel = Button('Cancel', 0, 40)
button_close = Button('Close', 0, 80)

# Credits
text_credits_egorka = Text('EgorkaGubarev - programmer', 0, 0)
text_credits_polina = Text('PolinaKP - designer, artist, composer', 0, 40)
button_credits_close = Button('Close', 0, 80)

# Menu
text_menu = Text('Space Program', 0, 0)
button_play = Button('Play', 0, 40)
button_tutorials = Button('Tutorials', 0, 80)
button_setting = Button('Settings', 0, 120)
button_credits = Button('Credits', 0, 160)
button_exit = Button('Exit', 0, 200)
