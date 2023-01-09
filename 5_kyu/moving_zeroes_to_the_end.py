def move_zeros(lst):
    res = [i for i in lst if i!=0]
    zero_count = lst.count(0)
    for _ in range(zero_count):
        res.append(0)
    return res