def filter_list(l):
    i_nt = []
    for i in l:
        if type(i) == int:
            i_nt.append(i) 
    return i_nt
    