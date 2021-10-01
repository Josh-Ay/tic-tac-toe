from random import choice
from brain import Brain
from board import Board
from clear import clear


def start_game():
    print("===========================TIC-TAC-TOE GAME====================================")

    brain, board = Brain(), Board()

    brain.display_instructions()
    brain.display_board(board.explanatory_board)

    valid_input = False
    user_marker, computer_marker, winner = "", "", None

    while not valid_input:
        user_answer = input("\nX or O? 😈: ")

        if user_answer.upper() == "X":
            valid_input, user_marker, computer_marker = True, "X", "O"
        elif user_answer.upper() == "O":
            valid_input, user_marker, computer_marker = True, "O", "X"
        else:
            print("Invalid input. Please enter 'x' or 'o'.")

    def play():
        nonlocal winner
        accept_input = True
        user_placement = 0

        while accept_input:
            try:
                if len(brain.available_options) != 0:
                    user_placement = int(input("Where would you like to play? "))
                else:
                    accept_input = False
            except ValueError:
                print("Please enter a number")
            else:
                if user_placement < 0:
                    print("Please enter a positive number")
                elif user_placement == 0:
                    print("Please enter a value greater than 0")
                elif user_placement > 9:
                    print("Please enter a number between 1 and 9")
                else:
                    if len(brain.available_options) != 0:
                        if brain.check_available_options(user_placement):
                            board.place_marker_in_board(user_placement - 1, user_marker)
                            brain.remove_option_from_board(user_placement)

                            if len(brain.available_options) != 0:
                                computer_placement = choice(brain.available_options)
                                board.place_marker_in_board(computer_placement - 1, computer_marker)
                                brain.remove_option_from_board(computer_placement)

                            clear(), brain.display_board(board.starting_board)

                            if brain.check_for_3_in_a_row(board.starting_board)[0]:
                                accept_input = False
                                winner = brain.check_for_3_in_a_row(board.starting_board)[1]

                        else:
                            print("Sorry, that spot is already taken.")
                    else:
                        accept_input = False

    play(), brain.display_winner(user_marker, winner)

    play_again = input("Would you like to play again? (y/n): ")

    if play_again.upper() == "Y":
        clear(), start_game()
    else:
        print("\nThank you for playing! ")


start_game()
