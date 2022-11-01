def count_positives_sum_negatives(arr):
    pov = 0
    neg = 0
    if arr == []:
        return []
    for i in arr:
        if i < 0:
            neg += i
        elif i > 0:
            pov += 1
    return [pov, neg]