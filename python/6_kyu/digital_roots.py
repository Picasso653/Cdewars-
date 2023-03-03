def digital_root(n):
    while n >= 10:
        n = sum([int(i) for i in str(n)])
    return n