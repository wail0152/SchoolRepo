def calcAverage(lst):
    return sum(lst) / len(lst)


def calcListAverage(lst):
    num = 0
    div = 0
    for i in lst:
        num += sum(i)
        div += len(i)
    return num / div
