def find_outlier(integers):
    odd_numbers = 0
    even_numbers = 0
    for i in integers:
        if i%2==0:
            even_numbers +=1
        else:
            odd_numbers += 1
    if odd_numbers == 1:
        for x in integers:
            if x%2==1:
                return x
    else:
        for y in integers:
            if y%2==0:
                return y