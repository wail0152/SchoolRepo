from Mastermind.definitions import *

game_modes = {0: "MAN VS COMPUTER", 1: "COMPUTER VS MAN"}
option = -1

while option != 0 and option != 1:
    try:
        option = int(input(f"Type 0 for {game_modes[0]} and 1 for {game_modes[1]}: "))
    except ValueError:
        print("Try again and input 0 or 1.\n")
print(f"You have chosen {game_modes[option]}.")


def man_vs_ai():
    check_end(current_column, shield_row)
    game_board[current_column] = get_moves()
    print_board()
    pins = get_feedback(game_board[current_column], shield_row)
    print(f"You have {pins[0]} black pin(s) and {pins[1]} white pin(s).")
    check_win(pins[0], "You have won!")


def ai_vs_man():
    check_end(current_column, shield_row)
    simple_strategy(current_column, shield_row)


def print_board():
    for column in range(len(game_board)):
        for row in range(len(game_board[column])):
            print(game_board[column][row], end="  ")
        print("")


shield_row = set_shield(option)
running = True
while running:
    if option == 0:
        man_vs_ai()
    else:
        ai_vs_man()
    current_column += 1
