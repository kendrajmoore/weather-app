import random


def flip():
    r = random()
    if r < 0.5:
        return "heads"
    else:
        return "tails"


print(flip())
