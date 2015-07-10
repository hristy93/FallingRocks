from field import Field
from game import Game
import gui


def main():
    """Initializes the game, ui and field and starts the game loop"""
    field = Field(1080, 800)
    game = Game(field)
    ui = gui.UserInterface(game)
    ui.main_loop()

if __name__ == '__main__':
    main()
