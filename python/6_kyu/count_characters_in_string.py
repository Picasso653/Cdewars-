def count(string):
    dix = {}
    for i in string:
        a = string.count(i)
        string.replace(i,'')
        dix.update({i:a})
    return dix