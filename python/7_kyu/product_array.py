def product_array(numbers):
    prod = []
    for i in range(len(numbers)):
        m = 1
        for j in range(len(numbers)):
            if j != i:
                m *= numbers[j]
        prod.append(m)
    return prod