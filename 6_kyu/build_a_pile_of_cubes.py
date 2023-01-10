def find_nb(m):
    i = 0
    n = 0
    while i <m:
        i+= n**3
        n +=1
    if i==m:
        return n-1
    else: 
        return -1