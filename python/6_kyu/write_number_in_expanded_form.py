def expanded_form(num):
    txt = str(num)
    x = len(txt)
    res = []
    for i in range(x):
        if txt[i]=='0':
            continue
        else:
            res.append(txt[i] +"0"*(x-1-i))
    return " + ".join(res)