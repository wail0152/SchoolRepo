import random

colors = ['r', 'g', 'b', 'o', 'y', 'p']
shield_row = []
game_board_width = 10
game_board_height = 4
game_board = [[0 for x in range(game_board_height)] for y in range(game_board_width)]


def set_shield(shield):
    return shield


def rand_shield():
    return random.sample(colors, 4)
