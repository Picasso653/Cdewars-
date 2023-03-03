def to_jaden_case(string):
    d = string.lower()
    a = d.split()
    jaden_cased = []
    for i in a:
        b = str.upper(i[0])
        c = i.replace(i[0],b,1)
        jaden_cased.append(c)
    return ' '.join(jaden_cased)