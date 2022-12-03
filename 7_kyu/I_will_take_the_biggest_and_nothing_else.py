def max_int_chain(n):
    if n < 5:
        return -1
    else:
        x = n // 2
        if n%2==0:
            c = x-1
            d = x+1
        else:
            c = x+1
            d = x
    return c*d