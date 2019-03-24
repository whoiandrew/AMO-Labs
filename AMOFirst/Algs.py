import math


def alg1(b, c):
    return str((b * math.sqrt(c)) / math.pow(2, b) - (c * math.sqrt(b)) / math.pow(2, c))


def alg2(a, b, x):
    return str(a * math.pow(x, 3) - b * math.pow(x, 2)) if (x > 0) else str(b * math.pow(x, 3) + a * math.pow(x, 2))


def alg3(n1, n2):
    res1 = 1
    res2 = 0
    for j in range(1, n1 + 1): res1 *= math.factorial(j)
    for i in range(1, n2 + 1): res2 += math.factorial(i)
    return str(res1 - res2)
