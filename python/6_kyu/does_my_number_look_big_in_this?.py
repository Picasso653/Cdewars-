def narcissistic( value ):
    digit_sum = 0
    for digit in str(value):
        digit_sum += int(digit)**len(str(value))
    return value == digit_sum