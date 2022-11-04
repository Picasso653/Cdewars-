def is_square(n):  
    if n == 0:
        return True
    x, y = 1, n
    while x + 1 < y:
        mid = (x+y)//2
        if mid**2 < n:
            x = mid
        else:
            y = mid
    return n == x**2 or n == (x+1)**2
