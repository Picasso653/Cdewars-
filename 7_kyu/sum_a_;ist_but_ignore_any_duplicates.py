def sum_no_duplicates(l):
    x = []
    for i in l:
        if l.count(i) < 2:
            x.append(i)
    return sum(x)