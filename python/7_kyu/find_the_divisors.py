def divisors(integer):
    i = 2
    a = []
    while i < integer:
        if integer % i == 0:
            a.append(i)
        i += 1
    if a == []:
        return "{} is prime".format(integer)
    else:
        return a