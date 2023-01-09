def flatten_and_sort(array):
    a = []
    for n in array:
        for i in n:
            a.append(i)
            
    return sorted(a)