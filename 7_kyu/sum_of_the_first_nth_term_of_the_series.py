def series_sum(n):
    x = 1
    y = []
    i = 1
    while i < n+1:
        y.append(1/x)
        x += 3
        i += 1
    z = sum(y)
    return "{:.2f}".format(z)
    