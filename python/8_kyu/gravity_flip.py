def flip(d, a):
    if d == 'R':
        return sorted(a)
    else:
        a.sort(reverse = True)
        return a