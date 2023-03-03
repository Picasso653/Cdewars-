def row_sum_odd_numbers(n):
    x = (n ** 2) + (n-1)
    i = 0
    odd = []
    if n == 1:
        return n
    while i < n:
        odd.append(x)
        x -= 2
        i += 1
    return sum(odd)