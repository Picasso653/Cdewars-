def multiplication_table(size):
    table = []
    for i in range(1,size+1):
        line = []
        j = 1
        while j <= size:
            x = i*j
            line.append(x)
            j += 1
        table.append(line)
    return table