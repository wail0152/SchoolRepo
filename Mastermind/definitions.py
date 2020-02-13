import random

colors = ['r', 'g', 'b', 'o', 'y', 'p']
shield_row = []
game_board_width = 10
game_board_height = 4
game_board = [[0 for x in range(game_board_height)] for y in range(game_board_width)]
current_column = 0


def get_shield(shield):
    return shield


def rand_shield():
    return random.sample(colors, 4)


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
