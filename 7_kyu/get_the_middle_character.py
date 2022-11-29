def get_middle(s):
    n = len(s)
    my_list = list(s)
    if n%2==0:
        x = n // 2
        return my_list[x-1] + my_list[x]
    else:
        x = n // 2
        return my_list[x]