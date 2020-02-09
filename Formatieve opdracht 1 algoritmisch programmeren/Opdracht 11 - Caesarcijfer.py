def caesar_number():
    t = str(input("Geef een tekst: "))
    r = int(input("Geef een rotatite: "))
    new_string = ""
    for letter in t:
        new_string += chr(ord(letter) + r)
    return new_string


print(caesar_number())
