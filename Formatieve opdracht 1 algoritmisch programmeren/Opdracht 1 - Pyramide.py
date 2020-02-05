n = int(input("Hoe groot wil je de piramide maken? ")) * 2
t = 1


def forLoop(t, n):
    for i in range(n - 1):
        amount = min(t, n - t)
        for j in range(amount):
            print("*", end="")
        print("", end="\n")
        t += 1


def whileLoop(t, n):
    i = 0
    j = 0
    while i < n - 1:
        amount = min(t, n - t)
        while j < amount:
            print("*", end="")
            j += 1
        print("", end="\n")
        t += 1
        i += 1
        j = 0


def forLoopFlipped(t, n):
    s = ""
    for i in range(n - 1):
        amount = min(t, n - t)
        for j in range(amount):
            s += "*"
        print("{:>{}}".format(s, n//2))
        t += 1
        s = ""


forLoopFlipped(t, n)
