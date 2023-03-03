def factorial(n):
    product = 1
    for i in range(n):
        product *= (n-i)
    return product