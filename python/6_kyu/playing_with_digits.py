def dig_pow(n, p):
    x = 0
    for i,j in zip(str(n),range(p,p+len(str(n)))):
        x += int(i)**j
    return -1 if x%n != 0 else x/n