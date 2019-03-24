from random import *
import matplotlib.pyplot as plt
import math


def set_rand_arr(n):
    return [randrange(1, n + 1) for i in range(n)]


def show_plot():
    plt.plot([n for n in range(1,1000)], [n*math.log(n) for n in range(1,1000)])
    plt.xlabel("n")
    plt.ylabel("n*log(n)")
    plt.show()


def reader(file_name):
    with open(file_name, "r") as f:
        a = f.read()
        return list(map(int, a.split()))


def writer(file_name, arr):
    with open(file_name, "w") as f:
        for i in arr:
            f.write(f"{str(i)}\n")
