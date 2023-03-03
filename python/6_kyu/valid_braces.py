def valid_braces(string):
    open_braces = ['(', '{','[']
    closed_braces = [")",'}',"]"]
    dummy = []
    for i in string:
        if i in open_braces:
            a = open_braces.index(i)
            dummy.append(closed_braces[a])
        elif i in closed_braces:
            if dummy == [] or i != dummy[-1]:
                return False
            else:   dummy.pop()
    return not dummy