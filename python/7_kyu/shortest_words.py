def find_short(s):
    s = s.split()
    new_list =[]
    for i in s:
        k = len(i)
        new_list.append(k)
    return min(new_list)