def sort_array(source_array):
    odd_arranged = []
    for j in source_array:
        if j%2!=0:
            odd_arranged.append(j)
    x = sorted(odd_arranged)
    for s,p in enumerate(source_array):
        if p%2==0:
            x.insert(s,p)
    return x
        