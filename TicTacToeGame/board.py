import pygame
class TicTacToeBoard(object):

    def __init__(self, screen, game_state=None):
        """
        Constructor for the board object. Should initialize a variable called self.grid to store state.
        State is represented by a single list [a0, a1, a2..a8].
        They correspond to positions on the board as follows:

        a0 a1 a2
        a3 a4 a5
        a6 a7 a8

        game_state is an argument for the game state passed. It will be in the type described above for a state.
        If game_state is not None, initialize the board to the state in game_state.
        """
        pass

    def initialize_grid(self, screen):
        pass

    def draw(self, screen):
        pass

    def update_board(self, mpos):
        """
        Updates board-object's state based on mouseclick position - mpos.
        """
        pass

    def update_to_state(self, game_state):
        """
        Updates the board-object's state to the game_state passed where game state is of the type described
        in the constructor.
        """
        pass
