def high(x):
    num_list = []
    lsc = x.split(" ")
    for word in lsc:
        y = 0
        for letter in word:
            y += (ord(letter)-96)
        print(y)
        num_list.append(y)
    max_num = max(num_list)
    idx = num_list.index(max_num)
    return lsc[idx]