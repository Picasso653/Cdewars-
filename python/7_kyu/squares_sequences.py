def squares(x, n):
    y = x
    i = 0
    squares_ = [x]
    if n <= 0:
        return []
    else:
        while i < (n -1):
            y *= y
            squares_.append(y)
            i += 1
    return squares_