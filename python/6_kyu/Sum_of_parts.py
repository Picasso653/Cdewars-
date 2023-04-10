def parts_sums(ls):
    x = sum(ls)
    res_list = [x]
    for i in range(len(ls)):
        res_list.append(res_list[-1] - ls[i])
    return res_list