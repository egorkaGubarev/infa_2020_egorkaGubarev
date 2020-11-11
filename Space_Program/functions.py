def game_close(game):
    game.mode = 'close'


def game_credits(game):
    game.mode = 'credits'


def game_exit(game):
    game.status = 'exit'


def game_menu(game):
    game.mode = 'menu'


def game_tutorials(game):
    game.mode = 'tutorials'
