def power_of_two(x):
    return (x & (x-1)) == 0 if x > 0 else False