# global variables
game_still_going = True

# board
game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

winner = None

current_player = "X"


# display board
def display_board():
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])


# playing tic tac toe
def play_game():
    # print the initial board
    display_board()

    while game_still_going:
        # manage the moves of current player
        handle_turn(current_player)

        # check game status
        check_if_game_over()

        # change  to other player
        flip_player()

        # ending the game
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner is None:
        print("Tie game!")


# function for moves of a player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("choose a position from 1 to 9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if game_board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again!")

    game_board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        # there was no winner
        winner = None
    return


# checks if three in a column
def check_columns():
    global game_still_going

    # check if value of columns is same but not -
    column_1 = game_board[0] == game_board[3] == game_board[6] != "-"
    column_2 = game_board[1] == game_board[4] == game_board[7] != "-"
    column_3 = game_board[2] == game_board[5] == game_board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False
    # return winning player
    if column_1:
        return game_board[0]
    elif column_2:
        return game_board[1]
    elif column_3:
        return game_board[2]
    return


# checks if three in a column
def check_rows():
    global game_still_going

    # check if value of rows is same but not -
    row_1 = game_board[0] == game_board[1] == game_board[2] != "-"
    row_2 = game_board[3] == game_board[4] == game_board[5] != "-"
    row_3 = game_board[6] == game_board[7] == game_board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    # return winning player
    if row_1:
        return game_board[0]
    elif row_2:
        return game_board[3]
    elif row_3:
        return game_board[6]
    return


# checks if three diagonally
def check_diagonals():
    global game_still_going

    # check if value of diagonal is same but not -
    diagonal_1 = game_board[0] == game_board[4] == game_board[8] != "-"
    diagonal_2 = game_board[2] == game_board[4] == game_board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return winning player
    if diagonal_1:
        return game_board[0]
    elif diagonal_2:
        return game_board[2]
    return


def check_if_tie():
    global game_still_going

    if "-" not in game_board:
        game_still_going = False
    return


def flip_player():
    global current_player

    # change player token from current to next
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()