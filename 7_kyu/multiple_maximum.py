def max_multiple(divisor, bound):
    return max([n for n in range(1,bound+1) if n%divisor==0])