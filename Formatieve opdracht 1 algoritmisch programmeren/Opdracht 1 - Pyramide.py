try:
    input_num = int(input("Hoe groot wil je de piramide maken? ")) * 2
except ValueError:
    print("Start de programma opnieuw op en vul een juiste getal in.")
    exit()


def for_loop(n):
    t = 1
    for i in range(n - 1):
        amount = min(t, n - t)
        for j in range(amount):
            print("*", end="")
        print("", end="\n")
        t += 1


def while_loop(n):
    t = 1
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


def for_loop_flipped(n):
    t = 1
    s = ""
    for i in range(n - 1):
        amount = min(t, n - t)
        for j in range(amount):
            s += "*"
        print(f"{s:>{n//2}}")
        t += 1
        s = ""


for_loop_flipped(input_num)
