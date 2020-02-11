from Mastermind.definitions import *

game_modes = {0: "MAN VS COMPUTER", 1: "COMPUTER VS MAN"}
option = -1

while option != 0 and option != 1:
    try:
        option = int(input(f"Type 0 for {game_modes[0]} and 1 for {game_modes[1]}: "))
    except ValueError:
        print("Try again and input 0 or 1.\n")
print(f"You have chosen {game_modes[option]}.\n")


shield_row = set_shield(rand_shield())
print(shield_row)
running = True
while running:
    input("Wait")
