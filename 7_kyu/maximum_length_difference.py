def mxdiflg(a1, a2):
    if len(a1)==0 or len(a2)==0:
        return -1
    min_a1 = len(min(a1, key=len))
    max_a1 = len(max(a1, key=len))
    min_a2 = len(min(a2, key=len))
    max_a2 = len(max(a2, key=len))
    r1 = abs(min_a1 - max_a2)
    r2 = abs(min_a2 - max_a1)
    return r1 if r1 >= r2 else r2