from Mastermind.definitions import *

current_column = 0


def man_vs_ai(col):
    check_end()
    game_board[col] = get_moves()
    print_board()
    give_feedback()
    return col + 1


def check_end():
    if current_column == 10:
        print(f"The right combination is {shield_row}.")
        exit()


def check_win(rp):
    if rp == 4:
        print("You have won!")
        exit()


def get_moves():
    moves = str(input(f"\n({10 - current_column} move(s) left) Input 4 colors with a comma:\n")).split(",")
    if len(moves) < 4:
        print("Not enough colors given.")
        return get_moves()
    else:
        for move in moves:
            if move not in colors:
                print("Not a valid color has been given.")
                return get_moves()
    return moves


def print_board():
    for column in range(len(game_board)):
        for row in range(len(game_board[column])):
            print(game_board[column][row], end="  ")
        print("")


def give_feedback():
    red_pins = 0
    white_pins = 0
    visited = []

    for guess in range(len(game_board[current_column])):
        if game_board[current_column][guess] == shield_row[guess]:
            red_pins += 1
            visited.append(guess)

    for guess in range(len(game_board[current_column])):
        for color in range(len(shield_row)):
            if game_board[current_column][guess] == shield_row[color] and guess != color and color not in visited:
                white_pins += 1
                visited.append(color)

    print(f"You have {red_pins} red pins and {white_pins} white pins.")
    check_win(red_pins)
