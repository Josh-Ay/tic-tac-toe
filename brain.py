from board import Board


class Brain:
    def __init__(self):
        self.start = 0
        self.available_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.instructions = "\nINSTRUCTIONS: \n1. Choose either 'x' or 'o'." \
                            "\n2. Type in the number where you would like to place your marker('X' or 'O')" \
                            " in any of the spaces numbered from 1-9 like in the board shown below:\n"
        self.winner = ""

    def display_instructions(self):
        """ Displays the instructions for playing 'tic-tac-toe' """
        print(self.instructions)

    def display_board(self, board_to_display: Board()):
        """Displays the board passed in."""
        for index in range(0, len(board_to_display), 3):
            print("  |  ".join(board_to_display[index:index + 3]))
            if self.start < 2:
                print("--------------")

            self.start += 1

        self.start = 0

    def check_available_options(self, option):
        f"""Returns 'True' or 'False' depending on whether the {option} passed is still available. """
        if option in self.available_options:
            return True
        else:
            return False

    def remove_option_from_board(self, option):
        f"""Remove the {option} passed from the available options. """
        self.available_options.remove(option)

    def check_for_3_in_a_row(self, board: Board()):
        f"""Returns 'True' if there are 3 in a row and 'False' otherwise. """
        if board[0] == board[1] == board[2] and board[0] == board[1] == board[2] != " ":
            return True, board[0]

        elif board[3] == board[4] == board[5] and board[3] == board[4] == board[5] != " ":
            return True, board[3]

        elif board[6] == board[7] == board[8] and board[6] == board[7] == board[8] != " ":
            return True, board[6]

        elif board[0] == board[3] == board[6] and board[0] == board[3] == board[6] != " ":
            return True, board[0]

        elif board[1] == board[4] == board[7] and board[1] == board[4] == board[7] != " ":
            return True, board[1]

        elif board[2] == board[5] == board[8] and board[2] == board[5] == board[8] != " ":
            return True, board[2]

        elif board[0] == board[4] == board[8] and board[0] == board[4] == board[8] != " ":
            return True, board[0]

        elif board[2] == board[4] == board[6] and board[2] == board[4] == board[6] != " ":
            return True, board[2]

        else:
            return False, "none"

    def display_winner(self, marker_to_check, winning_marker):
        self.winner = winning_marker

        if marker_to_check == winning_marker:
            print("You win 😃🔥🔥!!")
        elif winning_marker is None:
            print("It's a draw 🤝.")
        else:
            print("Computer wins 😑")
