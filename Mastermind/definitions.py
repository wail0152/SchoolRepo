import random
import itertools

colors = ['r', 'g', 'b', 'o', 'y', 'p']
shield_row = []
game_board_width = 10
game_board_height = 4
game_board = [[0 for x in range(game_board_height)] for y in range(game_board_width)]
current_column = 0
color_combinations = sorted(list(itertools.product(colors, repeat=4)))


def set_shield(op):
    if op == 0:
        return get_shield(rand_shield())
    else:
        return get_moves(True)


def get_shield(shield):
    return shield


def rand_shield():
    return random.sample(colors, 4)


def check_end(col, sr):
    if col == 10:
        print(f"The right combination is {sr}.")
        exit()


def check_win(rp, s):
    if rp == 4:
        print(s)
        exit()


def get_moves(shield=False):
    moves = str(input(f"\n({10 - current_column} move(s) left) Input 4 colors with a comma:\n" if not shield else "\nSet the shield: ")).split(",")
    if len(moves) < 4:
        print("Not enough colors given.")
        return get_moves()
    else:
        for move in moves:
            if move not in colors:
                print("Not a valid color has been given.")
                return get_moves()
    return moves


def get_feedback(question, sr):
    red_pins = 0
    white_pins = 0
    visited = []

    for guess in range(len(question)):
        if question[guess] == sr[guess]:
            red_pins += 1
            visited.append(guess)

    for guess in range(len(question)):
        for color in range(len(sr)):
            if question[guess] == sr[color] and guess != color and color not in visited:
                white_pins += 1
                visited.append(color)

    return (red_pins, white_pins)


def simple_strategy(col, sr):
    pins = get_feedback(list(color_combinations[0]), sr)
    print("The computer guessed", list(color_combinations[0]))
    new_combinations = []

    for combination in color_combinations:
        if get_feedback(list(color_combinations[0]), list(combination)) == pins:
            new_combinations.append(combination)

    color_combinations.clear()
    color_combinations.extend(new_combinations)

    check_win(pins[0], f"The computer won in {col + 1} moves!")
