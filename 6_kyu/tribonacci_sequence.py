def tribonacci(signature, n):
    x = [a for a in signature ]
    for i in range(2,n-1):
        y = x[i]
        y += x[i-1] + x[i-2]
        x.append(y)
    return x if n>3 else [signature[j] for j in range(n)]

tribonacci([1,2,3], 10)