def solve(s):
    upper = 0
    lower = 0
    number = 0
    special = 0
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower +=1
        elif i.isnumeric():
            number +=1
        else:   special +=1
    return [upper, lower, number, special]