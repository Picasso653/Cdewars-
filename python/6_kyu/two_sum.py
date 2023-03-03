def two_sum(numbers, target):
    for i, j in enumerate(numbers):
        x = target - j
        if x in numbers and numbers.index(x) != i:
            return [i, numbers.index(target-j)]