def find_uniq(arr):
    return  [i for i in set(arr) if arr.count(i) == 1][0]