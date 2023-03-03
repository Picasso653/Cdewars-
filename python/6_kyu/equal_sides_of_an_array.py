def find_even_index(arr):
    for i in range(0,len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1