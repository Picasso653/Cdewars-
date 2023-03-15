def parse(data):
    x = 0
    result = []
    for i in data:
        if i == 'i': x += 1
        if i == 'd': x -= 1
        if i == 's': x *= x
        if i == 'o': result.append(x)
    return result