def largest(n,xs):
    largest_arranged = sorted(xs, reverse=True)
    x = slice(n)
    max_num = largest_arranged[x]
    return sorted(max_num)