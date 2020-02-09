import random
min_rand = 0
max_rand = 10
rand_num = random.randint(min_rand, max_rand)

try:
    inputNum = int(input(f"Raad het getal tussen {min_rand} en {max_rand}: "))
    while inputNum != rand_num:
        inputNum = int(input("Fout geraden probeer het nogmaals: "))
except ValueError:
    print("Vul een getal in!")
    exit()

print(f"Goed gedaan het getal was inderdaad {rand_num}!")
