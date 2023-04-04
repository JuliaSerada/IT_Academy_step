def count_even_element(ls):
    count = 0
    for i in ls:
        if i % 2 == 0:
            count += 1
    return count
