from game import Game

game = Game()

game.setup()
while game.mode != 'exit':
    game.update_logic()
    game.update_graphics()
    game.update_information()
    game.translate()
game.save_settings()
