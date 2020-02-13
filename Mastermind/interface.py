from Mastermind.definitions import *

game_modes = {0: "MAN VS COMPUTER", 1: "COMPUTER VS MAN"}
option = -1

while option != 0 and option != 1:
    try:
        option = int(input(f"Type 0 for {game_modes[0]} and 1 for {game_modes[1]}: "))
    except ValueError:
        print("Try again and input 0 or 1.\n")
print(f"You have chosen {game_modes[option]}.")


def man_vs_ai(col):
    check_end()
    game_board[col] = get_moves()
    print_board()
    give_feedback()
    return col + 1


def ai_vs_man(col):
    check_end()
    game_board[col] = get_moves()
    print_board()
    give_feedback()
    return col + 1


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
    return (red_pins, white_pins)


shield_row = get_shield(rand_shield())
running = True
while running:
    if option == 0:
        current_column = man_vs_ai(current_column)
    else:
        current_column = ai_vs_man(current_column)
