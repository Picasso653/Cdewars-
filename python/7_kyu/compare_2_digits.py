def compare(a, b):
    x = str(a)
    y = str(b)
    len_x = len(set(x))
    len_y = len(set(y))
    count = 0
    if a == b:
        return '100%'
    if len_x >= len_y:
        for i in range(len_y):
            if y[i] in x:
                count += 50
    else:
        for i in range(len_x):
            if x[i] in y:
                count += 50
    return str(count)+"%"
    # I miss coding in python


