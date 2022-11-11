def get_positions(n):
    p1 = (n % 3)
    p2 = ((n // 3) % 3)
    p3 = ((n // 9) % 3)
    return (p1, p2, p3)