def unique_in_order(iterable):
    result = []
    for item in iterable:
        if len(result) == 0 or item != result[-1]:
            result.append(item)
    return result
            