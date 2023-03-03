def count_sheep(n):
    if n<1:
        return ''
    count = ''
    for i in range(1,n+1):
        count += f"{str(i)} sheep..."
    return count