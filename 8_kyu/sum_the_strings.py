def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif b == "":
        sum = int(a)
        return str(sum)
    elif a == "":
        sum =  int(b)
        return str(sum)
    else:
        sum = int(a) + int(b)
    return str(sum)