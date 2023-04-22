def sum_factorial(lst):
    return sum([fact(i) for i in lst])
    
def fact(n):
    prod = 1
    while n != 1:
        prod *= n
        n -=1
    return prod