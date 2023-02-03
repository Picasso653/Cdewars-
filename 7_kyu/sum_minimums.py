def sum_of_minimums(numbers):
    x = 0
    for i in numbers:
        x += min(i)
    return x