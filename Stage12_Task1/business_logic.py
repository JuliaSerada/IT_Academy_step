def is_sorted_asc(ls):
    return all(ls[i] <= ls[i + 1]
               for i in range(len(ls) - 1))
