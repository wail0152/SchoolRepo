string1 = str(input("Geef een string: "))
string2 = str(input("Geef een string: "))


def check_different_char_index(s1, s2):
    index = -1
    shortest_string = s2 if (len(s1) > len(s2)) else s1
    for i in range(len(shortest_string)):
        if s1[i] != s2[i]:
            index = i
            break
    return index


print("Het eerste verschil zit op index: " + str(check_different_char_index(string1, string2)))
