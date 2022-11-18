def invert(lst):
    neg_numbers = []
    for number in lst:
        negate = number * -1
        neg_numbers.append(negate)
    return neg_numbers