def printer_error(s):
    colour_spectrum = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    err = ''
    for i in s:
        if i not in colour_spectrum:
            err += i
    return str(len(err))+'/'+ str(len(s))