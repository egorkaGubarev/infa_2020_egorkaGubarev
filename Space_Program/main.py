from game import Game

game = Game()

game.setup()
while game.status != 'exit':
    game.update_logic()
    game.update_graphics()
