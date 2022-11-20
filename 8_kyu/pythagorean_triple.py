def pythagorean_triple(integers):
    k = max(integers)
    q =integers.remove(k)
    l = max(integers)
    m = min(integers)
    return k**2 == (l**2 + (m**2))