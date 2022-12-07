def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    result = numbers.copy()
    result.remove(min(numbers))
    return result