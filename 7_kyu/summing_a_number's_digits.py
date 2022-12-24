def sum_digits(number):
    return sum([int(x) for x in str(abs(number))])