def persistence(n):
    a = 0
    while n >= 9:
        x = 1
        for i in str(n):
            x *= int(i)
        a+=1
        n = x
    return a