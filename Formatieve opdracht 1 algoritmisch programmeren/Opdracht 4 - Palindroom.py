def checkPalindroomSelf(s):
    newString = ""
    for i in s:
        newString = i + newString
    return newString


def checkPalindroomLib(s):
    return "".join(list(reversed(s)))

