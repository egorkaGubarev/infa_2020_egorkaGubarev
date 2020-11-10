from game import Game

game = Game()

while game.status != 'exit':
    game.update_logic()
