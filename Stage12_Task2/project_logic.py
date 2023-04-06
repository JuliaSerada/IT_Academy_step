
def is_mirror(ls):
    num = len(ls)
    return all(ls[i] == ls[num - 1 - i]
               for i in range(num // 2))
