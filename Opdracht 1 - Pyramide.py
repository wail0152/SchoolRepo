n = int(input("Hoe groot wil je de piramide maken? ")) * 2
t = 1

for i in range(n - 1):
    amount = min(t, n - t)
    for j in range(amount):
        print("*", end="")
    print("", end="\n")
    t += 1
