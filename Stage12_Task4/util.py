import random


def rand_init(ls, a=0, b=100):
    for i in range(len(ls)):
        ls[i] = random.randint(a, b)


def convert(ls):
    msg = " "
    for item in ls:
        msg += str(item) + " "
    return msg


def create_list(size, value=0):
    ls = []
    for _ in range(size):
        ls.append(value)
    return ls
