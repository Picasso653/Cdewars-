def binary_array_to_number(arr):
    str_arr = []
    for i in arr:
        s = str(i)
        str_arr.append(s) 
    a = ''.join(str_arr)
    return int(a,2)