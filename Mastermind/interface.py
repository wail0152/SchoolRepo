from Mastermind.definitions import *

game_modes = {0: "MAN VS COMPUTER", 1: "COMPUTER VS MAN"}
ai_modes = {0: "simple strategy", 1: "worst case strategy", 2: "own strategy"}
game_option = -1
ai_option = -1

while game_option != 0 and game_option != 1:
    try:
        game_option = int(input(f"\nType 0 for {game_modes[0]} and 1 for {game_modes[1]}: "))
    except ValueError:
        print("Try again and input 0 or 1.\n")
print(f"You have chosen {game_modes[game_option]}.")

if game_option == 1:
    while ai_option != 0 and ai_option != 1 and ai_option != 2:
        try:
            ai_option = int(input(f"\nType 0 for {ai_modes[0]}, 1 for {ai_modes[1]} or 2 for {ai_modes[2]}: "))
        except ValueError:
            print("Try again and input 0, 1 or 2.\n")
    print(f"You have chosen {ai_modes[ai_option]}.")


def man_vs_ai():
    check_end(current_column, shield_row)
    game_board[current_column] = get_moves(current_column)
    print_board()
    pins = get_feedback(game_board[current_column], shield_row)
    print(f"You have {pins[0]} black pin(s) and {pins[1]} white pin(s).")
    check_win(current_column, pins[0])


def ai_vs_man():
    check_end(current_column, shield_row)
    if ai_option == 0:
        simple_strategy(current_column, shield_row, color_combinations[0])
    elif ai_option == 1:
        worst_case(current_column, shield_row)
    elif ai_option == 2:
        own_strategy(current_column, shield_row, color_combinations[0])


def print_board():
    for column in range(len(game_board)):
        for row in range(len(game_board[column])):
            print(game_board[column][row], end="  ")
        print("")


shield_row = set_shield(current_column, game_option)
running = True
while running:
    if game_option == 0:
        man_vs_ai()
    else:
        ai_vs_man()
    current_column += 1
