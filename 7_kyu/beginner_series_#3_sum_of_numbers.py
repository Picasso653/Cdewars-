def get_sum(a,b):
    addition = 0
    if a>b:
        for i in range(b,a+1):
            addition += i
    else:
        for i in range(a,b+1):
            addition += i
    return addition