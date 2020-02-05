fn = 0


def fibonacci(n):
    return 1 if n == 1 or n == 2 else fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(9))
