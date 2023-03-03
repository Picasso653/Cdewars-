def find_next_square(sq):
    import math
    x = math.sqrt(sq)
    if x.is_integer():
        return (x+1)**2
    else:
        return -1
