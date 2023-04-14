def second_symbol(s, symbol):
    first_index = s.find(symbol)
    if first_index == -1:
        return -1
    second_index = s.find(symbol, first_index + 1)
    if second_index == -1:
        return -1
    return second_index
