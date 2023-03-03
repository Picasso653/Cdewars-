def calculate_years(principal, interest, tax, desired):
    y = 0
    while principal < desired:
        x = interest * principal
        z = x - (tax * x)
        principal += z
        y += 1
    return y
    raise NotImplementedError("TODO: calculate_years")
