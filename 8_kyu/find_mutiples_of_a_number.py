def find_multiples(integer, limit):
    multiple_list = []
    x = 0
    while x < limit:
        x += integer
        if x > limit:
            break
        else:
            multiple_list.append(x)
    return multiple_list