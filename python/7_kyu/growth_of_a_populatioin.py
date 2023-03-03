def nb_year(p0, percent, aug, p):
    import math
    i = 0
    while p0 < p:
        calc = p0 + (p0 *(percent/100)) + aug
        p0 = int(calc)
        i += 1
    return i