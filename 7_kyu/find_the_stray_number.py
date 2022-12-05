def stray(arr):
    arr.sort()
    n = len(arr)
    x = round(n / 2)
    first = arr[:x]
    first.reverse()
    second = arr[x:]
    for i in first:
        if i != first[0]:
            return i
    for j in second:
        if j != second[0]:
            return j