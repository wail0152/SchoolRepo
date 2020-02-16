import math


def vier_kwadraten(getal):
    for a in range(int(math.sqrt(getal / 4))):
        rest1 = getal - (a * a)
        for b in range(a, int(math.sqrt(getal / 3)) - (a * a)):
            rest2 = rest1 - (b * b)
            for c in range(b, int(math.sqrt(getal / 2)) - (b * b)):
                d = int(math.sqrt(rest2 - (c * c)))
                if a * a + b * b + c * c + d * d == getal:
                    return [a, b, c, d]


"""==============================================[ HU TESTRAAMWERK ]====================================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
from functools import reduce
import random
from time import perf_counter


def test_vier_kwadraten():
    # Simulated test cases
    for cnt in range(10):
        n = random.randrange(1, 10)

        for _ in range(4):
            n *= 10
            n += random.randrange(0, 10)

        lst = vier_kwadraten(n)
        assert n == reduce(lambda x, y: x + y, (map(lambda x: x ** 2, lst))), \
            f"Fout: vier_kwadraten({n}) geeft {lst}, maar {lst[0]}^2 + {lst[1]}^2 + {lst[2]}^2 + {lst[3]}^2 != {n}"


def test_vier_kwadraten_tijd():
    # Test cases
    testcases = [36624, 73504, 54296, 40923, 33504, 42627, 70798, 90815, 55367, 52699]

    for case in testcases:
        print(case)
        lst = vier_kwadraten(case)
        assert case == reduce(lambda x, y: x + y, (map(lambda x: x ** 2, lst))), \
            f"Fout: vier_kwadraten({case}) geeft {lst}, maar {lst[0]}^2 + {lst[1]}^2 + {lst[2]}^2 + {lst[3]}^2 != {case}"


if __name__ == '__main__':
    try:
        print("\x1b[0;32m")
        test_vier_kwadraten()
        print("Je functie vier_kwadraten(getal) werkt goed!\n")

        print("\x1b[0;30m")
        print("Timing van 10 getallen...")

        start_time = perf_counter()
        test_vier_kwadraten_tijd()
        delta_time = perf_counter() - start_time
        print(f"Totale tijd: {delta_time*1000:.0f}ms")

    except AssertionError as ae:
        print("\x1b[0;31m")
        print(ae)
