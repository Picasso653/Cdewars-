def find_difference(a, b):
    import math
    prod_a = math.prod(a)
    prod_b = math.prod(b)
    if prod_a <= prod_b:
        return (prod_b - prod_a)
    else:
        return (prod_a - prod_b)