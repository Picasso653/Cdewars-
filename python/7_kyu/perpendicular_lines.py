def perpendicular(n):
    x = 0
    d = 0
    i = 0
    if n < 2:
        return 0
    while i < n+1:
        x += d
        if i%2==1:
            d +=1
        i +=1
    return x