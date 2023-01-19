def longest_consec(strarr, k):
    n = len(strarr)
    x = []
    if k < 1 or k>n:
        return ''
    if strarr == []:
        return ''
    for i in range(n-k+1):
        x.append(''.join(strarr[i:i+k]))
    return max(x, key=len)