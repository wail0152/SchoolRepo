def checkDifferentCharIndex():
    index = -1
    string1 = str(input("Geef een string: "))
    string2 = str(input("Geef een string: "))
    shortestString = string2 if (len(string1) > len(string2)) else string1
    for i in range(len(shortestString)):
        if string1[i] != string2[i]:
            index = i
            break
    return index


print("Het eerste verschil zit op index: " + str(checkDifferentCharIndex()))
