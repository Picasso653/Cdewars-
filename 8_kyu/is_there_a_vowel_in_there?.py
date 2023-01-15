def is_vow(inp):
    y = []
    for x in inp:
        if x in (ord('a'),ord('e'),ord('i'),ord('o'),ord('u')):
            y.append(chr(x))
        else:
            y.append(x)
    return y