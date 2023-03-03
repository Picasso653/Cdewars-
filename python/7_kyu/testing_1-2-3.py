def number(lines):
    str_lst = []
    if lines == []:
        return []
    for i,j in enumerate(lines, 1):
         str_lst.append(f"{i}: {j}")
    return str_lst