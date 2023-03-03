def sort_by_length(arr):
    a = [(len(i),i) for i in arr]
    a.sort()
    return [b for c,b in a]