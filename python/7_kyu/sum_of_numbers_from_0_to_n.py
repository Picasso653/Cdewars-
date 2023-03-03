def show_sequence(n):
    if n==0: return "0=0"
    a = [str(i) for i in range(n+1)]
    b = sum([i for i in range(n+1)])
    return '+'.join(a) +' = '+ str(b) if n>0 else f"{str(n)}<0"