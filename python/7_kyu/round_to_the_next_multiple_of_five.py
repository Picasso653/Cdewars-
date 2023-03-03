def round_to_next5(n):
    q = n//5
    r = n%5
    return (q*5)+5 if r > 0 else n