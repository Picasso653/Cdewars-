def min_value(digits):
    a = set(digits)
    b = sorted(a)
    c = ''
    for i in b:
        c+= str(i)
    return int(c)  