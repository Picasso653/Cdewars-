def xo(s):
    numx = 0
    numo = 0
    for i in s:
        if i.lower() == 'x':
            numx += 1
        elif i.lower() == 'o':
            numo += 1
    return numx == numo