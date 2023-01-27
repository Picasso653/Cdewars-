def sum_dig_pow(a, b):
    res = []
    for i in range(a,b+1):
        digits = list(str(i))
        if i == sum([int(l)**j for j,l in enumerate(digits,1)]):
            res.append(i)
    return res