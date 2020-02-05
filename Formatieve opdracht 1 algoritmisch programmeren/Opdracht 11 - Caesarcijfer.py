def caesarNumber():
    t = str(input("Geef een tekst: "))
    r = int(input("Geef een rotatite: "))
    newString = ""
    for letter in t:
        newString += chr(ord(letter) + r)
    return newString


print(caesarNumber())
