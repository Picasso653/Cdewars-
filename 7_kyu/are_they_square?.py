import math
def is_square(arr):
    if arr == []:
        return None
    else:
        num_arr = len(arr)
        num_sqr = 0
        for i in arr:
            if math.sqrt(i) % 1 == 0:
                num_sqr += 1
        return (num_arr == num_sqr)
