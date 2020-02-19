import random
import itertools

colors = ['r', 'g', 'b', 'o', 'y', 'p']
shield_row = []
current_column = 0
game_board = [[0 for x in range(4)] for y in range(10)]
color_combinations = sorted(list(itertools.product(colors, repeat=4)))


def set_shield(col, op):
    if op == 0:
        return rand_shield()
    else:
        return get_moves(col, True)


def rand_shield():
    return random.sample(colors, 4)


def check_end(col, sr):
    if col == 10:
        print(f"The right combination is {sr}.")
        exit()


def check_win(col, black_pins):
    if black_pins == 4:
        print(f"The breaker won in {col + 1} moves!")
        exit()


def get_moves(col, breaker=False):
    moves = str(input(f"\n({10 - col} move(s) left) Input 4 colors with a comma:\n" if not breaker else "\nSet the shield: ")).split(",")
    for move in moves:
        if move not in colors or len(moves) < 4:
            print("Not enough colors given or not a valid color has been given.")
            return get_moves(col, breaker)
    return moves


def get_feedback(question, sr):
    black_pins = 0
    white_pins = 0
    visited_shield = []
    visited_question = []

    for question_index in range(len(sr)):
        if question[question_index] == sr[question_index]:
            black_pins += 1
            visited_shield.append(question_index)
            visited_question.append(question_index)

    for question_index in range(len(sr)):
        for shield_index in range(len(sr)):
            if question[question_index] == sr[shield_index] and shield_index not in visited_shield and question_index not in visited_question:
                white_pins += 1
                visited_shield.append(shield_index)
                visited_question.append(question_index)

    return (black_pins, white_pins)


def simple_strategy(col, sr):
    pins = get_feedback(list(color_combinations[0]), sr)
    game_board[col] = color_combinations[0]
    print("The computer guessed", list(color_combinations[0]))
    new_combinations = []

    for combination in color_combinations:
        if get_feedback(color_combinations[0], combination) == pins:
            new_combinations.append(combination)

    color_combinations.clear()
    color_combinations.extend(new_combinations)

    check_win(col, pins[0])


def worst_case(col, sr):
    possible_combinations = {"0": {}, "1": {}, "2": {}, "3": {}, "4": {}}
    question_combinatios = [['r', 'r', 'r', 'r'], ['r', 'r', 'r', 'g'], ['r', 'r', 'g', 'g'], ['r', 'r', 'g', 'b'], ['r', 'g', 'b', 'o']]
    for com_ind in range(len(question_combinatios)):
        for color_index in range(len(color_combinations)):
            if str(get_feedback(question_combinatios[com_ind], color_combinations[color_index])) not in possible_combinations[str(com_ind)]:
                possible_combinations[str(com_ind)][str(get_feedback(question_combinatios[com_ind], color_combinations[color_index]))] = 1
            else:
                possible_combinations[str(com_ind)][str(get_feedback(question_combinatios[com_ind], color_combinations[color_index]))] += 1

    largest_partition = [0, 0, 0, 0, 0]
    for combo in possible_combinations:
        for possibility in possible_combinations[combo]:
            if possible_combinations[combo][possibility] > largest_partition[int(combo)]:
                largest_partition[int(combo)] = possible_combinations[combo][possibility]

    print(question_combinatios[largest_partition.index(min(largest_partition))])
