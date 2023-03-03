def sum_triangular_numbers(n):
    if n < 0:
        return 0
    i = 1
    sum_ = 0
    while i <= n:
        formula_ = (i *(i + 1))/2
        sum_ += formula_
        i += 1
    return sum_