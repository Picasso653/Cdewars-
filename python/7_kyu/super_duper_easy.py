def problem(a):
    if type(a) == int:
        return ((a * 50) + 6)
    elif type(a) == str:
        return 'Error'
    else:
        return ((a * 50) + 6)