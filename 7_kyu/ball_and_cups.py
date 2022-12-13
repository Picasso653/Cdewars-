def cup_and_balls(b, arr):
    for i in arr:
        if b in i:
            if b == i[0]:
                b = i[-1]
            else:
                b = i[0]
    return b