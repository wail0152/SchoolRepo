def count(lst, x):
    t = 0
    for i in lst:
        if i == x:
            t += 1
    return t


def difference(lst):
    biggest_diff = 0
    for i in range(len(lst) - 1):
        if abs(lst[i + 1]) - abs(lst[i]) > biggest_diff:
            biggest_diff = abs(lst[i + 1]) - abs(lst[i])
    return biggest_diff


def list_check(lst):
    cond = False
    if count(lst, 1) > count(lst, 0) and count(lst, 0) < 12:
        cond = True
    return cond

