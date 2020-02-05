import random
minRand = 0
maxRand = 10
randNum = random.randint(minRand, maxRand)

inputNum = int(input("Raad het getal tussen {} en {}: ".format(minRand, maxRand)))
while inputNum != randNum:
    inputNum = int(input("Fout geraden probeer het nogmaals: "))

print("Goed gedaan het getal was inderdaad {}!".format(randNum))
