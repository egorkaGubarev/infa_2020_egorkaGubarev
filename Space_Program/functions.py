def game_close(game):
    game.mode = 'close'


def game_close_cancel(game):
    game.mode = 'menu'


def game_exit(game):
    game.status = 'exit'
