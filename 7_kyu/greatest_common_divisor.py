def mygcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a