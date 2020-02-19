import random
import itertools

colors = ['r', 'g', 'b', 'o', 'y', 'p']
shield_row = []
current_column = 0
game_board = [[0 for x in range(4)] for y in range(10)]
color_combinations = sorted(list(itertools.product(colors, repeat=4)))
old_moves = []


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


def simple_strategy(col, sr, move):
    pins = get_feedback(move, sr)
    game_board[col] = move
    print("The computer guessed", move)
    new_combinations = []

    for combination in color_combinations:
        if get_feedback(move, combination) == pins:
            new_combinations.append(combination)

    color_combinations.clear()
    color_combinations.extend(new_combinations)

    check_win(col, pins[0])


def worst_case(col, sr):
    possible_combinations = {"0": {}, "1": {}, "2": {}, "3": {}, "4": {}}
    question_combinations = [['r', 'r', 'r', 'r'], ['r', 'r', 'r', 'g'], ['r', 'r', 'g', 'g'], ['r', 'r', 'g', 'b'], ['r', 'g', 'b', 'o']]
    test_combinations = [[4, 0, 0, 0], [3, 1, 0, 0], [2, 2, 0, 0], [2, 1, 1, 0], [1, 1, 1, 1]]

    for com_ind in range(len(question_combinations)):
        for color_index in range(len(color_combinations)):
            if str(get_feedback(question_combinations[com_ind], color_combinations[color_index])) not in possible_combinations[str(com_ind)]:
                possible_combinations[str(com_ind)][str(get_feedback(question_combinations[com_ind], color_combinations[color_index]))] = 1
            else:
                possible_combinations[str(com_ind)][str(get_feedback(question_combinations[com_ind], color_combinations[color_index]))] += 1

    largest_partition = [0, 0, 0, 0, 0]
    for combo in possible_combinations:
        for possibility in possible_combinations[combo]:
            if possible_combinations[combo][possibility] > largest_partition[int(combo)]:
                largest_partition[int(combo)] = possible_combinations[combo][possibility]

    indices = [i for i, v in enumerate(largest_partition) if v == min(largest_partition)]
    right_combination = ()
    counter = 0
    while right_combination == ():
        for indice in indices:
            letters_combination = test_combinations[indice]
            for combination in color_combinations:
                check_combination = [0, 0, 0, 0]
                check_index = 0
                for letter in set(combination):
                    check_combination[check_index] = combination.count(letter)
                    check_index += 1
                if sorted(check_combination, reverse=True) == letters_combination:
                    right_combination = combination
                    break
            else:
                continue
            break
        counter += 1
        indices = [i for i, v in enumerate(largest_partition) if v == min(largest_partition) + counter]

    simple_strategy(col, sr, right_combination)


def own_strategy(col, sr, move):
    pins = get_feedback(move, sr)
    game_board[col] = move
    print("The computer guessed", move)
    new_combinations = []

    for combination in color_combinations:
        if get_feedback(move, combination) == pins:
            new_combinations.append(combination)

    old_moves.append(move)

    for combination_index in range(len(new_combinations)):
        for old_move in old_moves:
            if get_feedback(move, old_move) != pins:
                new_combinations.remove(new_combinations[combination_index])

    color_combinations.clear()
    color_combinations.extend(new_combinations)

    check_win(col, pins[0])
