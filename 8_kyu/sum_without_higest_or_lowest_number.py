def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0
    s = sorted(arr)
    return  sum(s[1:-1])