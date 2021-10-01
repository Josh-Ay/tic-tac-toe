class Board:
    def __init__(self):
        self.explanatory_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.starting_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def place_marker_in_board(self, position, marker):
        self.starting_board[position] = marker
