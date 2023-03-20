def longest_repetition(chars):
    if chars == '':
        return ('', 0)
    max, n = '', 0
    num = 0
    for i in range(0,len(chars)-1):
        if chars[i] == chars[i+1]:
            num += 1
        else:
            num = 0
        if num+1 > n:
                max, n = chars[i], num+1
    return (max, n)