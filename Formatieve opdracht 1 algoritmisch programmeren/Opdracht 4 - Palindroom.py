def check_palindroom_self(s):
    new_string = ""
    for i in s:
        new_string = i + new_string
    return new_string == s


def check_palindroom_lib(s):
    return "".join(list(reversed(s))) == s

