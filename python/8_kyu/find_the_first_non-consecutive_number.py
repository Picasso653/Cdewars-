def first_non_consecutive(arr):
    if len(arr) < 2:
        return None
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1] + 1:
            return arr[i]
    return None