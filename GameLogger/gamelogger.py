class GameLogger(object):

    def __init__(self):
        pass

    def log_game(self, write_file):
        """
        Stores game states in the file sequentially.
        """
        pass

    def log_state(self, game_state, write_file):
        """
        Appends the game_state to the write_file
        """
        pass

    def get_game(self, read_file):
        """
        Reads the read_file and returns a list of game state objects in the order that they were put into the file.
        """
        pass

    def get_state(self, read_file, position=0):
        """
        Returns the game state object at the given position
        """
        pass
