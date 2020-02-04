def count(lst, x):
    t = 0
    for i in lst:
        if i == x:
            t += 1
    return t


def difference(lst):
    biggestDif = 0
    for i in range(len(lst) - 1):
        if abs(lst[i + 1]) - abs(lst[i]) > biggestDif:
            biggestDif = abs(lst[i + 1]) - abs(lst[i])
    return biggestDif


def listCheck(lst):
    cond = False
    if count(lst, 1) > count(lst, 0) and count(lst, 0) < 12:
        cond = True
    return cond

