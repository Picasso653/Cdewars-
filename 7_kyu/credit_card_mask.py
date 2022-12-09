def maskify(cc):
    dc = ''
    if len(cc) > 4:
        dc += '#' * (len(cc) - 4) + cc[-4:]
    else:
        return cc
    return dc