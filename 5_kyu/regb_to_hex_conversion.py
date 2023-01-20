def rgb(r, g, b):
    x = valid_number(r)
    y = valid_number(g)
    z = valid_number(b)
    r = hex_convert(x)
    g = hex_convert(y)
    b = hex_convert(z)
    return f"{r.zfill(2)}{g.zfill(2)}{b.zfill(2)}"
def hex_convert(a):
    return hex(a)[2:].upper()
def valid_number(n):
    if n>255:
        return 255
    elif n<0:
        return 0
    else: return n