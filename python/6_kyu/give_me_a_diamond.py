def diamond(n):
    if n % 2 == 0 or n < 1:
        return None

    diamond_str = ""
    for i in range(n):
        spaces = abs(n//2 - i)
        asterisks = n - 2*spaces
        diamond_str += " " * spaces + "*" * asterisks + "\n"
    
    return diamond_str